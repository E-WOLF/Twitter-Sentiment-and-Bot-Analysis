# this is a test page for the bot API... 
import botometer
import tweepy
from pprint import pprint

rapidapi_key = "RAPID API KEY" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': 'CONSUMER_KEY',
    'consumer_secret': 'CONSUMER SECRET',
    'access_token': 'ACCESS-TOKEN',
    'access_token_secret': 'TOKEN-SECRET',
    }

'''
Check to see if the user input above is a bot...
'''

botometer_api_url = 'https://botometer-pro.p.rapidapi.com'
bom = botometer.Botometer(botometer_api_url=botometer_api_url, wait_on_ratelimit=True, rapidapi_key=rapidapi_key, **twitter_app_auth)
result = bom.check_account('@probabot_')

pprint(result['scores']['universal'])