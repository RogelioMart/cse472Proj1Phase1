# read_retweets.py

# libraries
import tweepy

# local modules
import credentials

# authorization variables
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_KEY_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def retweetRecur(uScreenName, cntr, fPointer):
	
	if(cntr <= 5):
	
		cntr = cntr + 1
		
		threeCheck = 0
		
		#gets uScreenName 10 most recent tweets
		usersTweets = api.user_timeline(screen_name = uScreenName, count=10, include_rts = True, tweet_mode = 'extended')
		
		for tweetData in usersTweets:
			
			print("ID: " + str(tweetData.id))
			print(tweetData.created_at)
			print(tweetData.full_text)
			print("\n")
			
			
			#gets the retweets from one of the tweets
			retweets_list = api.retweets(tweetData.id)
			
			for rts in retweets_list:
			
				print(rts.user.screen_name)
			'''
				if(threeCheck > 2):#breaks out of the loop of 3 retweets hav already been found
					break
				
				if(len(retweets_list) >= 3):
					threeCheck = threeCheck + 1
					
					fPointer = open("edgeFile.txt", "a")
					
					f.write(uScreenName + " " + rts.user.screen_name + "\n")
					
					fPointer.close()
					
					retweetRecur(rts.user.screen_name, cntr, fPointer)
			'''
					
	return(0)
				
				
				
				
def main():
	
	fPointer = open("edgeFile.txt", "x")
	
	fPointer.close()
	
	retweetRecur("HIDEO_KOJIMA_EN", 0, fPointer)
	
main()

