import tweepy
import pandas as pd
from textblob import TextBlob
import settings
from sqlalchemy.exc import ProgrammingError
import csv


def post_tweet(msg):
    # print(api.me().name)
    api.update_status(msg)


# cot = csv.writer(open('file.csv', 'wb'))


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Do not process retweets
        # if status.retweeted_status:
        #     return
        # print(status.text)
        post_tweet('Thank you. How are you?')
        # cot.writerow(status.text)

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token_key, settings.access_token_secret)
api = tweepy.API(auth)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['@roshanlulu'])
