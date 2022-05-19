from kafka import KafkaConsumer
from pyspark.sql import Row, SparkSession
import ast
import sys
import yaml

topic = sys.argv[1]
pathWrite = sys.argv[2]

with open(r'../conf/conf.yaml') as file:
    conf = yaml.load(file)
    bootstrap_server = conf['bootstrap_servers']

spark = SparkSession.builder.getOrCreate()

consumer = KafkaConsumer(topic, bootstrap_servers=[bootstrap_server])
for tweet in consumer:
    values = tweet.value.decode('utf-8')
    listTwitter = ast.literal_eval(values)        
    df = spark.createDataFrame([Row(**i) for i in listTwitter])
    df.write.mode("overwrite").parquet(pathWrite)
    print("Dados ingestados com sucesso")