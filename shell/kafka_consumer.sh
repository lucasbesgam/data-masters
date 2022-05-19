#exemplo 
##param1 = topico kafka
##param2 = path para gravacao no hdfs
##bash kafka_consumer.sh santanderTweet /twitter/santander_analytics

spark-submit ../source/kafka_consumer.py "${1}" "${2}"