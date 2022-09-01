* Работоспособность программы проверить не удалось из-за сложностей, которые описаны ниже.
* Опыта работы со scala и avro до этого не было, что добавило сложности к выполнению задания.

Сложности, возникшие в ходе выпонения задания:

- В качестве первого варианта решения задания было выбрано использвать `apache.avro` класс [GenericRecordBuilder](https://avro.apache.org/docs/1.8.1/api/java/org/apache/avro/generic/GenericRecordBuilder.html) и далее с помощью его метода `set()` 
создать выходной файл на основе заданной схемы. При реализации данного решения возникли 2 проблемы:
1. Несмотря на прописанные import'ы, при запуске появлялась ошибка, скриншот которой показан ниже:
```scala 
import org.apache.avro.Schema
import org.apache.avro.generic
import org.apache.avro.generic.{GenericData, GenericDatumWriter}
import org.apache.avro.io.EncoderFactory
import org.apache.avro.generic.GenericRecordBuilder

val personAvroSchemaFilePath = "/home/ubuntu/sbetTest/а.avsc"
val schemaFile = new File(personAvroSchemaFilePath)

val parser: Schema.Parser = new Schema.Parser()
val schema: Schema = parser.parse(schemaFile)

val myRecordBuilder:GenericRecordBuilder = new GenericRecordBuilder(schema)
myRecordBuilder.set("endDdate1", "Operation1")....
```
 !["GenericRB error"](https://github.com/nbalol33/TestSberbank/blob/main/task3/GenericRB_error.png)
 
 **Решение проблемы, подходящее задаче, найти не удалось.**
 
  2. Не было понятно как с помощью set() взаимодействовать с вложенным полем `CollectionOperation`.
    
 - В качестве альтернатывного метода решения была выбрана библиотека [avro4s](https://github.com/sksamuel/avro4s), которая позволяет заполнять avro-файлы, используя
 `case classes`. Для этого исходный файл `a.avsc` был переписан в виде двух классов, по аналогии с блоком `Schemas` из доки, 
 а для заполнения взяты методы из блока `Input/Output`. **Решение крайне неоптимальное, но альтернатив найти не удалось.**
 
 В ходе этого решения также возникли сложности:
 1. Для использования библиотеки требовалось задать зависимости в gradle/sbt/maven (блок `Using avro4s in your project` доки). 
 Несмотря на успешную компиляцию maven (картинка ниже), система все равно не видела библиотеку (картинка ниже), аналогично с gradle.
 `pom.xml` файл `maven` и `build.gradle` файл `gradle` приложены в папке.
 
 ![maven1](https://github.com/nbalol33/TestSberbank/blob/main/task3/maven_compile_start.png) 
 ![maven2](https://github.com/nbalol33/TestSberbank/blob/main/task3/no%20library.png)
 
 **В итоге было принято решение дописать программу, как будто библиотека подключена и работает корректно, что в итоге не позволило проверить ее работоспособность.**
