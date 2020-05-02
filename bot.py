import botometer
import tweepy
import pprint

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
result = bom.check_account('@StephenCurry30')

print(result)