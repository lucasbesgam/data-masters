#!/usr/bin/env python

import tweepy
from kafka import KafkaProducer
import yaml
import sys

topic = sys.argv[1]
hashtag = sys.argv[2]

bootstrap_server = ''
api_key = ''
api_key_secret = ''
access_toket = ''
access_toket_secret = ''

with open(r'../conf/conf.yaml') as file:
    conf = yaml.load(file, Loader=yaml.FullLoader)
    bootstrap_server = conf['bootstrap_servers']
    api_key = conf['api_key']
    api_key_secret = conf['api_key_secret']
    access_toket = conf['access_toket']
    access_toket_secret = conf['access_toket_secret']

producer = KafkaProducer(bootstrap_servers=[bootstrap_server])

auth = tweepy.OAuth1UserHandler(
   api_key
    ,api_key_secret
    ,access_toket
    ,access_toket_secret
)

api = tweepy.API(auth)

cursor = tweepy.Cursor(
    api.search_tweets
    ,q='#{}'.format(hashtag)
    , tweet_mode='extended'
    , geocode='-23.5410028,-46.7773729,1200km').items()

tweets = []
for tweet in cursor:
    tweets.append({
        "full_text":tweet.full_text.encode()
    })

producer.send("santanderTweet", str(tweets).encode())

print("topico criado com sucesso")