import nltk
# this file has my twitter API credentials: consumer key, consumer secret, access token, access secret.
import config 
import tweepy
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import botometer
import requests

from textblob import TextBlob
# to run a wordcloud you need the proper software installed in system (I have visual studio)
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

auth = OAuthHandler(config.consumer_key,
                    config.consumer_secret)  # authentication object
# setting the access token & access token secret
auth.set_access_token(config.token,
                      config.token_secret)
api = tweepy.API(auth)  # creating API object that uses auth info

# documentation: https://github.com/IUNetSci/botometer-python


def is_bot(account):
    # now it's called rapidapi key
    rapidapi_key = config.rapidapi_key 
    twitter_app_auth = {
        'consumer_key': config.consumer_key,
        'consumer_secret': config.consumer_secret,
        'access_token': config.token,
        'access_token_secret': config.token_secret,
    }

    '''
    Check to see if the user input above is a bot...
    '''

    botometer_api_url = 'https://botometer-pro.p.rapidapi.com'
    bom = botometer.Botometer(botometer_api_url=botometer_api_url,
                              wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
    result = bom.check_account(account)
    return "{0:.2f}".format(result['scores']['universal'])


def percentage(part, whole):
    return 100 * float(part)/float(whole)


def get_tweet_sentiment(tweet):
    '''
    check the tweets sentiment passing through tweet
    using textblob's sentiment polarity analyzer.
    '''
    analysis = TextBlob(tweet.text)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    elif analysis.sentiment.polarity < 0:
        return 'negative'


def get_tweets(user_name, number_tweets_analyze=50):
    """
    important, function to pull tweets.
    """
    # tweets = []
    tweets = api.search(
        q=user_name, number_tweets_analyze=number_tweets_analyze)
    return tweets


def calc_user_sentiment_stats(user, count=50):
    '''
    function to tie everything together.
    '''
    tweets = get_tweets(user)

    pos_tweets = []
    neg_tweets = []
    neut_tweets = []

    for tweet in tweets:
        sentiment = get_tweet_sentiment(tweet)
        if sentiment == 'positive':
            pos_tweets.append(tweet)
        elif sentiment == 'negative':
            neg_tweets.append(tweet)
        elif sentiment == 'neutral':
            neut_tweets.append(tweet)

    # percentage of positive tweets
    positive = "{0:.2f}".format(100 * len(pos_tweets) / len(tweets))
    # percentage of negative tweets
    negative = "{0:.2f}".format(100 * len(neg_tweets) / len(tweets))
    # percentage of neutral tweets
    neutral = "{0:.2f}".format(100 * len(neut_tweets) / len(tweets))

    return positive, negative, neutral




'''
extrenuous code, below...
'''
# ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negitive']
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
    # for tweet in search_results:
    #     parsed_tweet = {}
    #     parsed_tweet['text'] = tweet.text
    #     parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)

    #     if tweet.retweet_count > 0:
    #         '''
    #         only append retweets once
    #         '''
    #         if parsed_tweet not in tweets:
    #             tweets.append(parsed_tweet)
    #         else:
    #             tweets.append(parsed_tweet)