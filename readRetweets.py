import tweepy

# Twitter API credentials
API_KEY = "wxlEOzKTqckeTZT6TFZAxynh8" # id that identifies API consumer
API_KEY_SECRET = "DWozBRNZXGrtiWEDwgvBQzsAJFuGwiwOfxVA7aVXBGq80mKYxf" # password to authenticate API consumer id
ACCESS_TOKEN =  "1304294097037987840-8I2YhFtByfIx4RwDQCe2ANcmPLUKmp" # id that identifies the test user assigned to our Twitter app
ACCESS_TOKEN_SECRET = "vcr9ZQwucmpRX5vUxkPDnazpcQc3GQPXfYJ093Vrj4E8b"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOOdHwEAAAAAHsSW%2FEONGXLg1umXXaiaeRk7etU%3DINP4FX4GwuEdfbK8hooawnepadIaxMUx8JKXjBKjs7x9DdGP9H"

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

kojimaID = 1278672884131483648

retweets_list = api.retweets(kojimaID)

for retweet in retweets_list:
	print(retweet.user.screen_name)