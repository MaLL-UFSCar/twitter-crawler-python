#python module to configure the twitter crawler for python

import ConfigParser

class ConfigTwitterCrawler():

    def __init__(self):
        
        config = ConfigParser.ConfigParser()
        config.read('../conf/twitter-crawler.conf')

        self.user_id_list = config.get('twitter-crawler','user_id_list').split(';')
