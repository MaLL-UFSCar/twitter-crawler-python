#python module to configure the twitter crawler for python

import ConfigParser

class ConfigTwitterCrawler():

    def __init__(self):
        
        config = ConfigParser.ConfigParser()
        config.read('../conf/twitter-crawler.conf')

        self.consumer_key = config.get('twitter-auth','consumer_key')
        self.consumer_secret = config.get('twitter-auth','consumer_secret')
        self.access_token = config.get('twitter-auth','access_token')
        self.access_token_secret = config.get('twitter-auth','access_token_secret')

        self.twitter_id_list = config.get('twitter-crawler','twitter_id_list').split(';')

        self.db_address = config.get('mongo-db','db_address')
        
