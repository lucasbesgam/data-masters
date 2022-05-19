#exemplo 
##param1 = topico kafka
##param2 = hashtag
##bash kafka_producer.sh santanderTweet santander

python3 ../source/kafka_producer.py "${1}" "${2}"