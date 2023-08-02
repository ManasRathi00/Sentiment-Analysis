
def get_tweets():
    import GetOldTweets3 as got
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('CoronaOutbreak') \
        .setSince("2020-01-01") \
        .setUntil("2020-04-01") \
        .setMaxTweets(1000)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Creating list of chosen tweet data
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

print(get_tweets())