import nltk
import twitter_credentials # this file has my twitter API credentials: consumer key, consumer secret, access token, access secret.
import tweepy
import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt
import botometer

from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # to run a wordcloud you need the proper software installed in system (I have visual studio)
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret) # authentication object
auth.set_access_token(twitter_credentials.token, twitter_credentials.token_secret) # setting the access token & access token secret 
api = tweepy.API(auth) # creating API object that uses auth info

# extract tweets from user

def percentage(part, whole):
    return 100 * float(part)/float(whole)

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

labels = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]', 'Neutral [' + str(neutral) + '%]']
sizes = [positive, neutral, negative]
colors =['yellow', 'red', 'blue']

patches, texts = plt.pie(sizes, colors = colors, startangle = 90)
plt.legend(patches, labels, loc ="best")
plt.title('General Sentiment for  ' + search + ' by analyzing ' + str(number_tweets_analyze)+ ' tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()

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

    

def is_bot(bot):
    '''
    Check to see if the user input above is a bot...
    '''

    bom = botometer.Botometer(wait_on_ratelimit=True,
                            mashape_key=mashape_key,
                            **api)

    # Check a single account by screen name
    result = bom.check_account(tweet)


        
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

