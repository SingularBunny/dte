import os
import sys
from unittest import TestSuite, TextTestRunner

from python.integration_test import StreamingTest


def suite():
    suite = TestSuite()
    # suite.addTest(SocketServerTest('test_socket_server'))
    # suite.addTest(DynamicClassLoadingTest('test_dynamic_loading'))
    suite.addTest(StreamingTest('test_streaming_mode'))
    # suite.addTest(StreamingTest('test_batch_mode'))
    return suite


jars = '/home/eugene/.ivy2/cache/com.google.code.findbugs/jsr305/jars/jsr305-3.0.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-yarn-common/jars/hadoop-yarn-common-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-core_2.10/jars/spark-core_2.10-1.6.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.directory.api/api-asn1-api/bundles/api-asn1-api-1.0.0-M20.jar,' \
       '/home/eugene/.ivy2/cache/io.dropwizard.metrics/metrics-json/bundles/metrics-json-3.1.2.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-yarn-client/jars/hadoop-yarn-client-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.scala-lang/scalap/jars/scalap-2.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.esotericsoftware.kryo/kryo/bundles/kryo-2.21.jar,' \
       '/home/eugene/.ivy2/cache/commons-el/commons-el/jars/commons-el-1.0.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.groovy/groovy-all/jars/groovy-all-2.4.13.jar,' \
       '/home/eugene/.ivy2/cache/org.sonatype.sisu.inject/cglib/jars/cglib-2.2.1-v20090111.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-mapreduce-client-core/jars/hadoop-mapreduce-client-core-2.6' \
       '.0-cdh5.10.0.jar,/home/eugene/.ivy2/cache/aopalliance/aopalliance/jars/aopalliance-1.0.jar,' \
       '/home/eugene/.ivy2/cache/com.amazonaws/aws-java-sdk-core/jars/aws-java-sdk-core-1.10.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-sql_2.10/jars/spark-sql_2.10-1.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.sun.jersey.contribs/jersey-guice/jars/jersey-guice-1.9.jar,' \
       '/home/eugene/.ivy2/cache/io.netty/netty-all/jars/netty-all-4.0.29.Final.jar,' \
       '/home/eugene/.ivy2/cache/com.esotericsoftware.reflectasm/reflectasm/jars/reflectasm-1.07-shaded.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-prefix-tree/jars/hbase-prefix-tree-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-hadoop-compat/jars/hbase-hadoop-compat-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-streaming_2.10/jars/spark-streaming_2.10-1.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.github.stephenc.high-scale-lib/high-scale-lib/jars/high-scale-lib-1.1.1.jar,' \
       '/home/eugene/.ivy2/cache/javax.servlet.jsp/jsp-api/jars/jsp-api-2.1.jar,' \
       '/home/eugene/.ivy2/cache/net.bytebuddy/byte-buddy-agent/jars/byte-buddy-agent-1.7.9.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.curator/curator-recipes/bundles/curator-recipes-2.7.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.httpcomponents/httpcore/jars/httpcore-4.4.1.jar,' \
       '/home/eugene/.ivy2/cache/tomcat/jasper-runtime/jars/jasper-runtime-5.5.23.jar,' \
       '/home/eugene/.ivy2/cache/com.fasterxml.jackson.core/jackson-annotations/jars/jackson-annotations-2.2.3.jar,' \
       '/home/eugene/.ivy2/cache/org.eclipse.jetty.orbit/javax.servlet/orbits/javax.servlet-3.0.0.v201112011016.jar,' \
       '/home/eugene/.ivy2/cache/commons-httpclient/commons-httpclient/jars/commons-httpclient-3.1.jar,' \
       '/home/eugene/.ivy2/cache/org.scalatest/scalatest_2.10/bundles/scalatest_2.10-3.0.3.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-launcher_2.10/jars/spark-launcher_2.10-1.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/parquet-jackson/jars/parquet-jackson-1.5.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/asm/asm/jars/asm-3.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.curator/curator-framework/bundles/curator-framework-2.7.1.jar,' \
       '/home/eugene/.ivy2/cache/xmlenc/xmlenc/jars/xmlenc-0.52.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-procedure/jars/hbase-procedure-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.avro/avro/bundles/avro-1.7.6-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.scala-lang/scala-compiler/jars/scala-compiler-2.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/parquet-column/jars/parquet-column-1.5.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.fasterxml.jackson.core/jackson-core/jars/jackson-core-2.2.3.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-client/jars/hadoop-client-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-yarn-api/jars/hadoop-yarn-api-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-core_2.10/jars/spark-core_2.10-1.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/parquet-common/jars/parquet-common-1.5.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.101tec/zkclient/jars/zkclient-0.7.jar,' \
       '/home/eugene/.ivy2/cache/org.jamon/jamon-runtime/jars/jamon-runtime-2.4.1.jar,' \
       '/home/eugene/.ivy2/cache/org.mortbay.jetty/jetty-util/jars/jetty-util-6.1.26.cloudera.4.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/parquet-encoding/jars/parquet-encoding-1.5.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/xml-apis/xml-apis/jars/xml-apis-1.3.04.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-common/jars/hbase-common-1.2.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/commons-collections/commons-collections/jars/commons-collections-3.2.2.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.jettison/jettison/bundles/jettison-1.1.jar,' \
       '/home/eugene/.ivy2/cache/com.thoughtworks.paranamer/paranamer/jars/paranamer-2.6.jar,' \
       '/home/eugene/.ivy2/cache/org.mockito/mockito-core/jars/mockito-core-2.13.0.jar,' \
       '/home/eugene/.ivy2/cache/org.tachyonproject/tachyon-underfs-local/jars/tachyon-underfs-local-0.8.2.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.mesos/mesos/jars/mesos-0.21.1-shaded-protobuf.jar,' \
       '/home/eugene/.ivy2/cache/org.slf4j/jcl-over-slf4j/jars/jcl-over-slf4j-1.7.5.jar,' \
       '/home/eugene/.ivy2/cache/org.json4s/json4s-ast_2.10/jars/json4s-ast_2.10-3.2.10.jar,' \
       '/home/eugene/.ivy2/cache/org.objenesis/objenesis/jars/objenesis-2.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.curator/curator-client/bundles/curator-client-2.7.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-thrift/jars/hbase-thrift-1.2.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/jline/jline/jars/jline-0.9.94.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-common/jars/hadoop-common-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.htrace/htrace-core/jars/htrace-core-3.2.0-incubating.jar,' \
       '/home/eugene/.ivy2/cache/org.slf4j/slf4j-log4j12/jars/slf4j-log4j12-1.7.6.jar,' \
       '/home/eugene/.ivy2/cache/com.lmax/disruptor/jars/disruptor-3.3.0.jar,' \
       '/home/eugene/.ivy2/cache/org.spark-project.protobuf/protobuf-java/jars/protobuf-java-2.4.1-shaded.jar,' \
       '/home/eugene/.ivy2/cache/io.dropwizard.metrics/metrics-graphite/bundles/metrics-graphite-3.1.2.jar,' \
       '/home/eugene/.ivy2/cache/com.google.protobuf/protobuf-java/bundles/protobuf-java-2.5.0.jar,' \
       '/home/eugene/.ivy2/cache/com.sun.jersey/jersey-core/bundles/jersey-core-1.9.jar,' \
       '/home/eugene/.ivy2/cache/commons-digester/commons-digester/jars/commons-digester-1.8.jar,' \
       '/home/eugene/.ivy2/cache/com.amazonaws/aws-java-sdk-sts/jars/aws-java-sdk-sts-1.10.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.commons/commons-math/jars/commons-math-2.1.jar,' \
       '/home/eugene/.ivy2/cache/org.slf4j/jul-to-slf4j/jars/jul-to-slf4j-1.7.5.jar,' \
       '/home/eugene/.ivy2/cache/com.clearspring.analytics/stream/jars/stream-2.7.0.jar,' \
       '/home/eugene/.ivy2/cache/org.xerial.snappy/snappy-java/bundles/snappy-java-1.1.2.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.thrift/libthrift/jars/libthrift-0.9.3.jar,' \
       '/home/eugene/.ivy2/cache/javax.xml.bind/jaxb-api/jars/jaxb-api-2.2.2.jar,' \
       '/home/eugene/.ivy2/cache/commons-lang/commons-lang/jars/commons-lang-2.6.jar,' \
       '/home/eugene/.ivy2/cache/org.mortbay.jetty/jetty/jars/jetty-6.1.26.cloudera.4.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.jackson/jackson-xc/jars/jackson-xc-1.8.8.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.jackson/jackson-mapper-asl/jars/jackson-mapper-asl-1.9.13.jar,' \
       '/home/eugene/.ivy2/cache/io.netty/netty/bundles/netty-3.10.5.Final.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/parquet-format/jars/parquet-format-2.1.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-aws/jars/hadoop-aws-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.ivy/ivy/jars/ivy-2.4.0.jar,' \
       '/home/eugene/.ivy2/cache/com.github.stephenc.findbugs/findbugs-annotations/jars/findbugs-annotations-1.3.9-1' \
       '.jar,/home/eugene/.ivy2/cache/commons-configuration/commons-configuration/jars/commons-configuration-1.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.httpcomponents/httpclient/jars/httpclient-4.4.1.jar,' \
       '/home/eugene/.ivy2/cache/com.sun.xml.bind/jaxb-impl/jars/jaxb-impl-2.2.3-1.jar,' \
       '/home/eugene/.ivy2/cache/commons-io/commons-io/jars/commons-io-2.4.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.janino/janino/jars/janino-2.7.8.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-server/jars/hbase-server-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-auth/jars/hadoop-auth-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.json4s/json4s-jackson_2.10/jars/json4s-jackson_2.10-3.2.10.jar,' \
       '/home/eugene/.ivy2/cache/org.scala-lang/scala-reflect/jars/scala-reflect-2.10.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-yarn-server-common/jars/hadoop-yarn-server-common-2.6.0' \
       '-cdh5.10.0.jar,/home/eugene/.ivy2/cache/org.apache.hbase/hbase-annotations/jars/hbase-annotations-1.2.0-cdh5' \
       '.10.0.jar,/home/eugene/.ivy2/cache/com.sun.jersey/jersey-server/bundles/jersey-server-1.9.jar,' \
       '/home/eugene/.ivy2/cache/io.dropwizard.metrics/metrics-jvm/bundles/metrics-jvm-3.1.2.jar,' \
       '/home/eugene/.ivy2/cache/javax.activation/activation/jars/activation-1.1.jar,' \
       '/home/eugene/.ivy2/cache/commons-codec/commons-codec/jars/commons-codec-1.9.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-mapreduce-client-shuffle/jars/hadoop-mapreduce-client' \
       '-shuffle-2.6.0-cdh5.10.0.jar,/home/eugene/.ivy2/cache/net.java.dev.jets3t/jets3t/jars/jets3t-0.9.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-thrift/jars/hbase-thrift-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-hdfs/jars/hadoop-hdfs-2.6.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/commons-beanutils/commons-beanutils/jars/commons-beanutils-1.7.0.jar,' \
       '/home/eugene/.ivy2/cache/org.spark-project.akka/akka-actor_2.10/jars/akka-actor_2.10-2.2.3-shaded-protobuf' \
       '.jar,/home/eugene/.ivy2/cache/org.spark-project.spark/unused/jars/unused-1.0.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-mapreduce-client-jobclient/jars/hadoop-mapreduce-client' \
       '-jobclient-2.6.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-server/jars/hbase-server-1.2.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/com.fasterxml.jackson.core/jackson-databind/jars/jackson-databind-2.2.3.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-network-common_2.10/jars/spark-network-common_2.10-1.6.0-cdh5' \
       '.10.0.jar,/home/eugene/.ivy2/cache/org.codehaus.jackson/jackson-core-asl/jars/jackson-core-asl-1.9.13.jar,' \
       '/home/eugene/.ivy2/cache/javax.servlet/servlet-api/jars/servlet-api-2.5.jar,' \
       '/home/eugene/.ivy2/cache/tomcat/jasper-compiler/jars/jasper-compiler-5.5.23.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-hadoop2-compat/jars/hbase-hadoop2-compat-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-streaming-kafka_2.10/jars/spark-streaming-kafka_2.10-1.6.0' \
       '-cdh5.10.0.jar,/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-yarn-server-nodemanager/jars/hadoop-yarn' \
       '-server-nodemanager-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.hamcrest/hamcrest-core/jars/hamcrest-core-1.3.jar,' \
       '/home/eugene/.ivy2/cache/com.typesafe/config/bundles/config-1.0.2.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.directory.server/apacheds-i18n/bundles/apacheds-i18n-2.0.0-M15.jar,' \
       '/home/eugene/.ivy2/cache/com.esotericsoftware.minlog/minlog/jars/minlog-1.2.jar,' \
       '/home/eugene/.ivy2/cache/junit/junit/jars/junit-4.12.jar,/home/eugene/.ivy2/cache/oro/oro/jars/oro-2.0.8.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-hadoop2-compat/jars/hbase-hadoop2-compat-1.2.0-cdh5.10.0' \
       '-tests.jar,/home/eugene/.ivy2/cache/com.intel.chimera/chimera/jars/chimera-0.9.2.jar,' \
       '/home/eugene/.ivy2/cache/org.json4s/json4s-core_2.10/jars/json4s-core_2.10-3.2.10.jar,' \
       '/home/eugene/.ivy2/cache/org.fusesource.leveldbjni/leveldbjni-all/bundles/leveldbjni-all-1.8.jar,' \
       '/home/eugene/.ivy2/cache/com.google.inject.extensions/guice-servlet/jars/guice-servlet-3.0.jar,' \
       '/home/eugene/.ivy2/cache/com.yammer.metrics/metrics-core/jars/metrics-core-2.2.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.avro/avro-ipc/jars/avro-ipc-1.7.6-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-annotations/jars/hadoop-annotations-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.spark-project.akka/akka-remote_2.10/bundles/akka-remote_2.10-2.2.3-shaded' \
       '-protobuf.jar,/home/eugene/.ivy2/cache/org.apache.zookeeper/zookeeper/jars/zookeeper-3.4.6.jar,' \
       '/home/eugene/.ivy2/cache/com.amazonaws/aws-java-sdk-kms/jars/aws-java-sdk-kms-1.10.6.jar,' \
       '/home/eugene/.ivy2/cache/log4j/log4j/bundles/log4j-1.2.17.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.jackson/jackson-jaxrs/jars/jackson-jaxrs-1.8.8.jar,' \
       '/home/eugene/.ivy2/cache/com.amazonaws/aws-java-sdk-s3/jars/aws-java-sdk-s3-1.10.6.jar,' \
       '/home/eugene/.ivy2/cache/commons-daemon/commons-daemon/jars/commons-daemon-1.0.13.jar,' \
       '/home/eugene/.ivy2/cache/com.google.code.gson/gson/jars/gson-2.2.4.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.kafka/kafka-clients/jars/kafka-clients-0.9.0-kafka-2.0.2.jar,' \
       '/home/eugene/.ivy2/cache/com.google.inject/guice/jars/guice-3.0.jar,' \
       '/home/eugene/.ivy2/cache/org.jruby.jcodings/jcodings/jars/jcodings-1.0.8.jar,' \
       '/home/eugene/.ivy2/cache/org.tachyonproject/tachyon-underfs-hdfs/jars/tachyon-underfs-hdfs-0.8.2.jar,' \
       '/home/eugene/.ivy2/cache/xerces/xercesImpl/jars/xercesImpl-2.9.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-client/jars/hbase-client-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.htrace/htrace-core4/jars/htrace-core4-4.0.1-incubating.jar,' \
       '/home/eugene/.ivy2/cache/com.fasterxml.jackson.module/jackson-module-scala_2.10/bundles/jackson-module' \
       '-scala_2.10-2.2.3.jar,/home/eugene/.ivy2/cache/commons-beanutils/commons-beanutils-core/jars/commons' \
       '-beanutils-core-1.8.0.jar,/home/eugene/.sbt/boot/scala-2.10.7/lib/scala-library.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-mapreduce-client-jobclient/jars/hadoop-mapreduce-client' \
       '-jobclient-2.6.0-cdh5.10.0.jar,/home/eugene/.ivy2/cache/io.dropwizard.metrics/metrics-core/bundles/metrics' \
       '-core-3.1.2.jar,/home/eugene/.ivy2/cache/org.apache.directory.server/apacheds-kerberos-codec/bundles/apacheds' \
       '-kerberos-codec-2.0.0-M15.jar,/home/eugene/.ivy2/cache/org.tukaani/xz/jars/xz-1.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.commons/commons-compress/jars/commons-compress-1.4.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-hdfs/jars/hadoop-hdfs-2.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.roaringbitmap/RoaringBitmap/bundles/RoaringBitmap-0.5.11.jar,' \
       '/home/eugene/.ivy2/cache/net.sf.py4j/py4j/jars/py4j-0.9.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/chill_2.10/jars/chill_2.10-0.5.0.jar,' \
       '/home/eugene/.ivy2/cache/org.jruby.joni/joni/jars/joni-2.1.2.jar,' \
       '/home/eugene/.ivy2/cache/net.jpountz.lz4/lz4/jars/lz4-1.3.0.jar,' \
       '/home/eugene/.ivy2/cache/com.ning/compress-lzf/bundles/compress-lzf-1.0.3.jar,' \
       '/home/eugene/.ivy2/cache/commons-logging/commons-logging/jars/commons-logging-1.2.jar,' \
       '/home/eugene/.ivy2/cache/com.jcraft/jsch/jars/jsch-0.1.42.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.kafka/kafka_2.10/jars/kafka_2.10-0.9.0-kafka-2.0.2.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/chill-java/jars/chill-java-0.5.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.avro/avro-mapred/jars/avro-mapred-1.7.6-cdh5.10.0-hadoop2.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.directory.api/api-util/bundles/api-util-1.0.0-M20.jar,' \
       '/home/eugene/.ivy2/cache/commons-net/commons-net/jars/commons-net-3.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-common/jars/hadoop-common-2.6.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/org.codehaus.janino/commons-compiler/jars/commons-compiler-2.7.8.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-mapreduce-client-app/jars/hadoop-mapreduce-client-app-2.6.0' \
       '-cdh5.10.0.jar,/home/eugene/.ivy2/cache/net.razorvine/pyrolite/jars/pyrolite-4.9.jar,' \
       '/home/eugene/.ivy2/cache/org.spark-project.akka/akka-slf4j_2.10/bundles/akka-slf4j_2.10-2.2.3-shaded-protobuf' \
       '.jar,/home/eugene/.ivy2/cache/com.google.guava/guava/bundles/guava-14.0.1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-sql_2.10/jars/spark-sql_2.10-1.6.0-cdh5.10.0-tests.jar,' \
       '/home/eugene/.ivy2/cache/org.slf4j/slf4j-api/jars/slf4j-api-1.7.6.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.avro/avro-ipc/jars/avro-ipc-1.7.6-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-hadoop-compat/jars/hbase-hadoop-compat-1.2.0-cdh5.10.0-tests' \
       '.jar,/home/eugene/.ivy2/cache/org.apache.spark/spark-network-shuffle_2.10/jars/spark-network-shuffle_2.10-1.6' \
       '.0-cdh5.10.0.jar,/home/eugene/.ivy2/cache/com.sun.jersey/jersey-client/bundles/jersey-client-1.9.jar,' \
       '/home/eugene/.ivy2/cache/commons-cli/commons-cli/jars/commons-cli-1.2.jar,' \
       '/home/eugene/.ivy2/cache/org.tachyonproject/tachyon-underfs-s3/jars/tachyon-underfs-s3-0.8.2.jar,' \
       '/home/eugene/.ivy2/cache/com.twitter/parquet-hadoop/jars/parquet-hadoop-1.5.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.tachyonproject/tachyon-client/jars/tachyon-client-0.8.2.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-unsafe_2.10/jars/spark-unsafe_2.10-1.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hbase/hbase-common/jars/hbase-common-1.2.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/com.jamesmurty.utils/java-xmlbuilder/jars/java-xmlbuilder-0.4.jar,' \
       '/home/eugene/.ivy2/cache/javax.inject/javax.inject/jars/javax.inject-1.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.hadoop/hadoop-mapreduce-client-common/jars/hadoop-mapreduce-client-common' \
       '-2.6.0-cdh5.10.0.jar,/home/eugene/.ivy2/cache/org.apache.hbase/hbase-protocol/jars/hbase-protocol-1.2.0-cdh5' \
       '.10.0.jar,/home/eugene/.ivy2/cache/org.apache.xbean/xbean-asm5-shaded/bundles/xbean-asm5-shaded-4.4.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.spark/spark-catalyst_2.10/jars/spark-catalyst_2.10-1.6.0-cdh5.10.0.jar,' \
       '/home/eugene/.ivy2/cache/net.bytebuddy/byte-buddy/jars/byte-buddy-1.7.9.jar,' \
       '/home/eugene/.ivy2/cache/org.scalactic/scalactic_2.10/bundles/scalactic_2.10-3.0.3.jar,' \
       '/home/eugene/.ivy2/cache/javax.xml.stream/stax-api/jars/stax-api-1.0-2.jar,' \
       '/home/eugene/.ivy2/cache/org.uncommons.maths/uncommons-maths/jars/uncommons-maths-1.2.2a.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.commons/commons-math3/jars/commons-math3-3.4.1.jar,' \
       '/home/eugene/.ivy2/cache/com.beust/jcommander/jars/jcommander-1.72.jar,' \
       '/home/eugene/.ivy2/cache/org.apache.commons/commons-lang3/jars/commons-lang3-3.3.2.jar,' \
       '/home/eugene/.ivy2/cache/com.sun.jersey/jersey-json/bundles/jersey-json-1.9.jar,' \
       '/home/eugene/IdeaProjects/sd360/hbase-coprocessors/target/scala-2.10/hbase-coprocessors_2.10-0.54.jar'
if __name__ == '__main__':
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars {} ' \
                                        '--conf spark.driver.userClassPathFirst=true ' \
                                        '--master local[32] pyspark-shell'.format(jars)
    os.environ['PYSPARK_PYTHON'] = sys.executable

    runner = TextTestRunner()
    runner.run(suite())
