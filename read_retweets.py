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
	
'''
def retweetRecur(userID, cntr):
	
	if (cntr <= 5)
		cntr = cntr + 1
		
		get a list of the user's tweets.
		
		iterate through the tweet list only 3 times
		
			make a list of all users who retweeted current tweet.
			if(tweet has retweets)
				tweet iterator countr ++
				
				write to a txt file the user's screen name and who currently retweeted them.
				
				retweetRecur(retweeter's ID, cntr)
			else 
				go to next tweet. (to pull this off you'll need another number that iterates through that dictionary)
		
			
		
	return(0)
		
'''

def retweetRecur(uScreenName, cntr, fPointer):
	
	if(cntr <= 5)
		cntr = cntr + 1
		
		threeCheck = 0
		
		tweetIter = 0
		
		rtsIter = 0
		
		usersTweets = api.user_timeline(screen_name = uScreamName, count=10, include_rts = True, tweet_mode = 'extended')
		
		while((threeCheck < 3) && (tweetIter < 10)):
			
			retweets_list = api.retweets(usersTweets[tweetIter].id)
			
			if(len(retweets_list) >= 3):
				threeCheck = threeCheck + 1
				tweetIter = tweetIter + 1
				
				fPointer = open("edgeFile.txt", "a")
				
				f.write(uScreenName + " " + retweets_list[rtsIter] + "\n")
				
				fPointer.close()
				
				retweetRecur(, cntr, fPointer)
				
			else:
				tweetIter = tweetIter + 1
				
		return(0)
				
				
				
				
def main():
	
	fPointer = open("edgeFile.txt", "x")
	
	retweetRecur(, 0, fPointer)
	
main()