# read_retweets.py

# libraries
import tweepy

# local modules
import config


# authorization variables
auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# get mentions
def recursion(screen_name, counter, max_depth, mentions, tweets, file_ptr):
    
    if counter < max_depth:
    
        counter += 1
        mention_count = 0
        
        # get user's tweets
        users_tweets = api.user_timeline(screen_name = screen_name, count=tweets, include_mentions = True, tweet_mode = 'extended')
        
        # get first mention in each tweet
        for status in users_tweets:
        
            # if tweet is a mention, store it and call mention_recursion() on first mention
            if mention_count < mentions:
            
                mention_count += 1
                
                # get the screen name of the user's first mention
                if len(status.entities['user_mentions']) > 0:
                    first_mention = status.entities['user_mentions'][0]['screen_name']
                    
                    # store mention data
                    config.NETWORK_MENTIONS_LIST.append(status)
                    print_to_file(screen_name, first_mention, file_ptr)
                    
                    # call recursion on first mention
                    mention_recursion(first_mention, counter, max_depth, mentions, tweets, file_ptr)


# print the mentions to a log file
def print_to_file(user_name, mention_name, file_ptr):
    file_ptr = open(config.EDGE_LOG_PATH, "a")
    file_ptr.write(user_name + " " + mention_name + "\n")
    file_ptr.close()