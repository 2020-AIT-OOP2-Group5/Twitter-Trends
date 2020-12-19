from pytrends.request import TrendReq
import pandas
import numpy
from twitter import *
import re
import tweepy
from flask import Flask, request, render_template, redirect
import datetime
import json

pytrends = TrendReq()
trend = pytrends.trending_searches(pn='japan')

json_open = open('Twitter_Key&Token.json', 'r')
twitter_key_token = json.load(json_open)

print(twitter_key_token['AT'])

twitter = Twitter(auth=OAuth(
    twitter_key_token['AT'], twitter_key_token['AS'], twitter_key_token['CK'], twitter_key_token['CS']))


def getTrends():
    results = twitter.trends.place(_id=23424856)
    Pre_Twitter_list = []
    Tweet_Twitter_list = []
    for location in results:
        for trend in location["trends"]:
            if trend["tweet_volume"] != None:
                Pre_Twitter_list.append(trend["name"])
                Tweet_Twitter_list.append(trend["tweet_volume"])

    twitter_list = ' '.join(Pre_Twitter_list[:5])
    tweet_list = ' '.join(map(str, Tweet_Twitter_list[:5]))
    print(twitter_list)
    print(tweet_list)

    twitter_list = twitter_list.split(" ")
    tweet_list = tweet_list.split(" ")

    auth = tweepy.OAuthHandler(
        twitter_key_token["CK"], twitter_key_token["CS"])
    auth.set_access_token(twitter_key_token["AT"], twitter_key_token["AS"])
    api = tweepy.API(auth)

    top_tweet = ["", "", "", "", ""]
    tweet_text = ""
    max_retweet = 0

    for i in range(5):

        tweets = api.search(
            q=twitter_list[i], count=tweet_list[i], tweet_mode='extended')
        for tweet in tweets:
            if max_retweet < tweet.retweet_count:
                tweet_text = tweet.full_text.replace('\n', '')
                max_retweet = tweet.retweet_count

        # top_tweet.append(tweet_text)
        top_tweet[i] = tweet_text.split(':', 1)[1]
        max_retweet = 0
        print(top_tweet[i])

    time = datetime.datetime.now()

    return [time, twitter_list, tweet_list, top_tweet]

#print(time.strftime('%Y年%m月%d日 %H:%M:%S'))

# ここからweb


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', time=time, twitter_list=twitter_list, tweet_list=tweet_list, top_tweet=top_tweet)


@app.route('/koushin')
def koushin():
    global time, twitter_list, tweet_list, top_tweet
    results = getTrends()
    time = results[0]
    twitter_list = results[1]
    tweet_list = results[2]
    top_tweet = results[3]
    return redirect("/")


if __name__ == "__main__":
    results = getTrends()
    time = results[0]
    twitter_list = results[1]
    tweet_list = results[2]
    top_tweet = results[3]
    app.run(debug=True)
