#main script to collect tweets from specific accounts and
#save them as mongoDB records

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

twitter_id_list = list

for twitter_id in twitter_id_list:
    status_list = api.user_timeline(user_id=twitter_id)

    for status in status_list:
        #add status to db



