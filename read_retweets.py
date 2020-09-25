# read_retweets.py

# libraries
import tweepy

# local modules
import credentials

# authorization variables
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_KEY_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

kojima_ID = 1278672884131483648

retweets_list = api.retweets(kojima_ID)

for retweet in retweets_list:
	print(retweet.user.screen_name)