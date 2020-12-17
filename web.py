from flask import Flask, request, render_template, redirect
import tweepy
from operator import itemgetter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', tweet_list=tweet_list)

@app.route('/kousin')
def koushin():

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
