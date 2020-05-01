import re
import json
from flask import Flask, render_template, request
import user_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        query = request.form['query']
        count = request.form['count']
        tweets = get_tweets(user_name = user_name, number_tweets_analyze = number_tweets_analyze)
        ptweets = [tweet for tweet in tweets if tweet['sentiment']=='positive']
        ntweets = [tweet for tweet in tweets if tweet['sentiment']=='negitive']

        # percentage of positive tweets
        positive = "{0:.2f}".format(100 * len(ptweets) / len(tweets))
        # percentage of negative tweets
        negative = "{0:.2f}".format(100 * len(ntweets) / len(tweets))
        # percentage of neutral tweets
        neutral = "{0:.2f}".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))
        results = [positive, negative, neutral, query, count]
        print(query)

        return render_template('index.html,',  error=None)
    else:
        return render_template('index.html')
        
        
        
        
        
    #     try:
    #         user_name = request.form['name'] # Name, city, state are all variables from the 
    #         user = user_name
    #         tweet_count = number_tweets_analyze

            
            
            
    #         if is_bot: # need to figure this out...
    #             return render_template('result.html', place_name=place, station_name=station_name, wheelchair_accessible="")
            
    #         else:
    #             return render_template('result.html', place_name=place, station_name=station_name, wheelchair_accessible="Not")
    #     except:
    #         return render_template('hello.html', error=True)
    # return render_template('hello.html', error=None)
