#main script to collect tweets from specific accounts and
#save them as mongoDB records

import tweepy
import pprint
import pymongo

from twitter_crawler_config import ConfigTwitterCrawler
from pymongo import MongoClient
from datetime import datetime

#get object for configuration
tc_config = ConfigTwitterCrawler()

#get database address from configuration
db_address = tc_config.db_address

#connection to mongo database
conn = MongoClient(db_address)

db_tweet = conn['tweet']

#twitter authentication
auth = tweepy.OAuthHandler(tc_config.consumer_key, tc_config.consumer_secret)
auth.set_access_token(tc_config.access_token, tc_config.access_token_secret)

#get api object
api = tweepy.API(auth)

#get list of twitter ids from configuration
twitter_id_list = tc_config.twitter_id_list

#id_tweet should be unique in the database
db_tweet.tweet.create_index([('id_tweet',pymongo.ASCENDING)], unique=True)

for twitter_id in twitter_id_list:				#for each twitter id
    status_list = api.user_timeline(screen_name=twitter_id) 	#get the list of tweets

    for status in status_list:					#for each list of tweets

        try:

            #insert tweets into database
            db_tweet.tweet.insert_one(
                {
                    'screen_name': status.author.screen_name, 
                    'text': status.text,
                    'id_tweet' : status.id,
                    'created_at': status.created_at
                }
            )
            print "inserted tweet with id ",status.id
        except pymongo.errors.DuplicateKeyError:
            print "failed attempt to duplicate id ",status.id
 
