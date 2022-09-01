from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from kafka.structs import OffsetAndMetadata
import json

TOPIC_NAME = "taskS1"
# Kafka server
KAFKA_HOST = "localhost"
KAFKA_PORT = "9092"
group_id = 'cons'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_HOST + ":" + KAFKA_PORT,
                                    group_id = group_id,
                                    auto_offset_reset='earliest',
                                    enable_auto_commit=False)
                                    #value_deserializer=lambda x: x.encode('utf-8'))

def main():
    tp0 = TopicPartition(TOPIC_NAME, 0)
    tp1 = TopicPartition(TOPIC_NAME, 1)
    print("consumer is listening....")
    consumer.unsubscribe()
    while True:
        consumer.assign([tp0])
        _ = consumer.poll(1000, max_records=1)
        number = ""
        for tp0, messages in _.items():
            for message in messages:
                number = message.value.decode('utf-8')
                offset = message.offset

        consumer.assign([tp1])
        _ = consumer.poll(1000, max_records=1)
        for tp1, messages in _.items():
            for message in messages:
                value = message.value.decode('utf-8')
                #offset = message.offset

        # my_consumer.seek(1, key_position)
        # my_consumer.consumer.commit()

        pair = str(number)+": "+ value
        #sample = str(number)
        print(pair)
        with open('result.txt', 'a') as fp:
            fp.write(number +": "+ value+ '\n')
            #fp.write(number +": "+'\n')

        consumer.commit({
            tp0: OffsetAndMetadata(offset+1, None)
        })
        consumer.commit({
            tp1: OffsetAndMetadata(offset+1, None)
        })

if __name__ == '__main__':
    main()
