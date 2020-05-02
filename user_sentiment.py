import nltk
import twitter_credentials # this file has my twitter API credentials: consumer key, consumer secret, access token, access secret.
import tweepy
import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt
import botometer
import requests 

from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # to run a wordcloud you need the proper software installed in system (I have visual studio)
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

rapidapi_key = "74b8c6af71mshdcaf5182ae5b714p1c90fcjsn4ed7590773a9"
auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) # authentication object
auth.set_access_token(twitter_credentials.token, twitter_credentials.token_secret) # setting the access token & access token secret 
api = tweepy.API(auth) # creating API object that uses auth info

# documentation: https://github.com/IUNetSci/botometer-python

def is_bot(bot):
    rapidapi_key = "74b8c6af71mshdcaf5182ae5b714p1c90fcjsn4ed7590773a9" # now it's called rapidapi key
    twitter_app_auth = {
    'consumer_key': 'bhMOINHjn7hJrSuw207fISCuZ',
    'consumer_secret': 'dNPYY23HgRyCvzsOvEFkQ1XYJdemSczBAD7wFx4XOVC3vDlqPY',
    'access_token': '708013197060657152-MOq9K2WaueJJRuxPWwhsJbVeCDccr42',
    'access_token_secret': 'ACHgS2VAI5udSOSkxYjdBbj3YIgXObEWQHPs0FCSVDUFo',
    }

    '''
    Check to see if the user input above is a bot...
    '''

    botometer_api_url = 'https://botometer-pro.p.rapidapi.com'
    bom = botometer.Botometer(botometer_api_url=botometer_api_url, wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
    result = bom.check_account(tweet)
    return

def percentage(part, whole):
    return 100 * float(part)/float(whole)

# extract tweets from user

def get_tweet_sentiment(tweet):
	'''
	check the tweets sentiment passing through tweet
	using textblob's sentiment polarity analyzer.
	'''
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

        #need help with this
        # code for pie chart https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html



def get_tweets(user_name, number_tweets_analyze=50):
    """
    important, function to pull tweets.
    """
    t = []
    tw = self.api.search(q=user_name, number_tweets_analyze = number_tweets_analyze)
    for tweet in tw:
        parsed_tweet = {}

        parsed_tweet['text'] = tweet.text
        parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)

        if tweet.retweet_count > 0:
            '''
            only append retweets once
            '''
            if parsed_tweet not in t:
                t.append(parsed_tweet)
            else:
                t.append(parsed_tweet)
    return t

   

        
def find_twitter_user():
    '''
    function to tie everything together.
    '''
    return get_tweets(*get_tweet_sentiment(tweet)) # not sure on this one. 










# # these variables call the percentage function to divide the cumulative polarity scores by the number of tweets analyzed. 
# positive = percentage(positive, number_tweets_analyze)
# negative = percentage(negative, number_tweets_analyze)
# neutral = percentage(neutral, number_tweets_analyze)
# polarity = percentage(polarity, number_tweets_analyze)

# # to two decimals 
# positive = format(positive, '.2f')
# negative = format(negative, '.2f')
# neutral = format(neutral, '.2f')

# print('General Sentiment for  ' + search + ' by analyzing ' + str(number_tweets_analyze)+ ' tweets.')

# # uses the cumulative polarity to return the general sentiment of the sample 
# if (polarity == 0):
#     print('general sentiment is neutral')
# elif(polarity < 0):
#     print('general sentiment is negative')
# elif(polarity > 0):
#     print('general sentiment is positive')

'''
this is the pie chart.... stretch goal... 
'''

# labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]', 'Neutral [' + str(neutral) + '%]']
# sizes = [positive, neutral, negative]
# colors =['yellow', 'red', 'blue']

# patches, texts = plt.pie(sizes, colors = colors, startangle = 90)
# plt.legend(patches, labels, loc ="best")
# plt.title('General Sentiment for  ' + search + ' by analyzing ' + str(number_tweets_analyze)+ ' tweets.')
# plt.axis('equal')
# plt.tight_layout()
# plt.show() # look up how to show the image. 


# botometer documentation
'''
# Check a single account by screen name
    result = bom.check_account(tweet)

# from the botometer documentation
url = "https://botometer10.p.rapidapi.comhttps//osome-botometer.p.rapidapi.com"

headers = {
    'x-rapidapi-host': "botometer10.p.rapidapi.com",
    'x-rapidapi-key': "74b8c6af71mshdcaf5182ae5b714p1c90fcjsn4ed7590773a9"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

'''