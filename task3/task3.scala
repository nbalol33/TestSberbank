import java.io.File
import com.sksamuel.avro4s.AvroOutputStream
import scala.util.Random

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.FileSystem
import org.apache.hadoop.fs.Path

//create case classes based on a.avsc

case class CollectionOperation(op_type: String)
case class TestAvroEntry(endDate: String, paramValues: Seq[CollectionOperation])

//add values
val result: Array[String]
var data: String

for (w <- 99999)
{   
    val stringF = Iterator.continually(Random.nextPrintableChar()).filter(_.isLetterOrDigit).take(5).mkString
    val stringS = Iterator.continually(Random.nextPrintableChar()).filter(_.isLetterOrDigit).take(5).mkString
    if r.nextInt(10) < 5:
        val values = TestAvroEntry(stringF, stringS)
        //val values = TestAvroEntry("my_EndDate1", Seq(CollectionOperation("op_type1")))
    else if r.nextInt(10) < 5:
        val values = TestAvroEntry(null, stringS)
    else if r.nextInt(10) < 5:
        val values = TestAvroEntry(stringF, null)
    else
        val values = TestAvroEntry(null, null)     

val schema = AvroSchema[TestAvroEntry]
val result = result :+ values
}
val os = AvroOutputStream.data[TestAvroEntry].to(new File("/home/ubuntu/sbetTest/test.avro")).build()
os.write(result)
os.flush()
os.close()

//copy to hdfs
val hadoopConf = new Configuration()
val hdfs = FileSystem.get(hadoopConf)

val srcPath = new Path("/home/ubuntu/sbetTest/test.avro")
val destPath = new Path("hdfs://localhost:9000/user/sberTest")

hdfs.copyFromLocalFile(srcPath, destPath)
