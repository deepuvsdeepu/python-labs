from textblob import TextBlob
import tweepy
import statistics
from configparser import ConfigParser
from pathlib import Path
# load from installed module
# from utils import cfg_loader
from modules.config_util.config_util import cfg_loader

cfg = cfg_loader.loadsecrets()['TWITTER_KEY']
auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
auth.access_token = cfg['access_token']
auth.access_token_secret = cfg['access_secret']

api = tweepy.API(auth)

def evaluate_sentiment(input_text, doLog=False):
    sentiment = TextBlob(input_text).sentiment
    if doLog:
        print('Sentiment score for the input text is : ' + str(sentiment))
    return sentiment


def analyse_tweets(search_text, sample_size=1):
    sentiment_scores = []
    for _ in range(sample_size):
        public_tweets = api.search(search_text, result_type='populator')
        for tweet in public_tweets:
            # print(tweet.text, '\n')
            # print(''.join('-' for i in range(0, len(tweet.text))))
            sentiment_scores.append(evaluate_sentiment(tweet.text))

    polarity_scores = [x.polarity for x in sentiment_scores]
    # print('Polarity scores: ' + str(polarity_scores))
    final_polarity = statistics.variance(polarity_scores)
    # final_polarity = average(polarity_scores)
    print("Final polarity:", final_polarity)
    print("Tweets related to: " + search_text + " are mostly " +
          ('positive' if final_polarity >= 0 else 'negative'))


# evaluate_sentiment('President Trump is using a global pandemic as cover to exact political revenge against the Intelligence Community Inspector', True)
# evaluate_sentiment('It took Obama 8 years to fix 8 years of Bush but it took Trump only 3 years to undo 244 years of the USA', True)
analyse_tweets('obama')
analyse_tweets('trump')
