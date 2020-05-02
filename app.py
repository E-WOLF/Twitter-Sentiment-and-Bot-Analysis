import re
import os
import json
from flask import Flask, render_template, request
from user_sentiment import is_bot, calc_user_sentiment_stats

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        account = request.form['account']
        count = request.form['count']
        positive, negative, neutral = calc_user_sentiment_stats(user=account, count=count)
        bot_percent = is_bot(account)
        user_tweet_data = {
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'bot_percent': bot_percent
        }

        return render_template('result.html', user_tweet_data=user_tweet_data)
    
    else:
        return render_template('index.html')
