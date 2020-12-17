from pytrends.request import TrendReq
import pandas, numpy
from twitter import *
import re
import tweepy
from flask import Flask, request, render_template, redirect
import datetime

pytrends = TrendReq()
trend = pytrends.trending_searches(pn = 'japan')

CK = "6c3ueDtot5JInpVt11Ji2c7wh"
CS = "8Yw06209wso7ykMK6rEET461QDUXEKhtF6EQ7rVqQRnc1TWqeH"
AT = "1336913672803733504-hQgzG4BiShULaBoQ8Meno3YQJjltC7"
AS = "ahbjvKy9mYn0lvlAdJUjmp0A2cetfpeXWMFA3iW6UNOlT"

twitter = Twitter(auth = OAuth(AT,AS,CK,CS))
results = twitter.trends.place(_id = 23424856)

Pre_Twitter_list = []
Tweet_Twitter_list = []
for location in results:
        for trend in location["trends"]:
            if trend["tweet_volume"] != None:            
                Pre_Twitter_list.append(trend["name"])
                Tweet_Twitter_list.append(trend["tweet_volume"])

twitter_list = ' '.join(Pre_Twitter_list[:5])
tweet_list = ' '.join(map(str,Tweet_Twitter_list[:5]))
print(twitter_list)
print(tweet_list)

twitter_list = twitter_list.split(" ")
tweet_list = tweet_list.split(" ")



auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

top_tweet = []

for i in range(5):
    tweets = api.search(q=twitter_list[i], count=1, tweet_mode='extended')
    for tweet in tweets:
        top_tweet.append([tweet.retweet_count,tweet.full_text.replace('\n','')])


print(top_tweet)

time = datetime.datetime.now()

print(time.strftime('%Y年%m月%d日 %H:%M:%S'))

#ここからweb

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', tweet_list=tweet_list)

if __name__ == "__main__":
    app.run(debug=True)
