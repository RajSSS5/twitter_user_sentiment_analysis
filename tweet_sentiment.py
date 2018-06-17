import tweepy
from textblob import TextBlob
import config

#Include necessary authorization variables in config
auth = tweepy.OAuthHandler(config.api_key,  config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def TweetRating(name):
	avg = 0
	total = 0
	for tweet in tweepy.Cursor(api.user_timeline, screen_name= name, include_rts = False).items():
		total += 1
		analysis = TextBlob(tweet.text)
		avg += analysis.sentiment.polarity
	avg /= total
	return total, avg
def main():

	total = 0
	avg = 0
	name = input("Enter Twitter Username: ")
	try:
		total,avg = TweetRating(name)
	except:
		print("ERROR: Invalid Username")
		return
	print("On a scale from -1 to 1,", name + '\'s', "last", total, "Tweets have a rating of: ", avg)
if __name__ == '__main__':
    main()