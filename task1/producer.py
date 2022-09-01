from kafka import KafkaProducer
from time import sleep
import random
import string

# Kafka topic name
TOPIC_NAME = "taskS1"

# Kafka server
KAFKA_HOST = "localhost"
KAFKA_PORT = "9092"
producer = KafkaProducer(bootstrap_servers=KAFKA_HOST + ":" + KAFKA_PORT)

def main():
    while True:
        number = random.randint(0,100000)
        word = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        send_number = producer.send(TOPIC_NAME, str(number).encode('utf-8'), partition = 0)
        send_word = producer.send(TOPIC_NAME, word.encode('utf-8'), partition = 1)
        sleep(1)

        print(f"{number}: {word}")

if __name__ == '__main__':
    main()


