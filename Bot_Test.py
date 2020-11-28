# Bot_Test.py
# Dataset: botometer-feedback-2019
#   direct download: (https://botometer.osome.iu.edu/bot-repository/datasets/botometer-feedback-2019/botometer-feedback-2019.tar.gz)
#   source: https://botometer.osome.iu.edu/bot-repository/datasets.html


# libraries
import pandas as pd
import os

# local modules
import config
import json

# Constants
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
BOT_DATASET_JSON_PATH = DIR_PATH + r"\botometer-feedback-2019_tweets.json"
BOT_DATASET_CSV_PATH = DIR_PATH + r"\botometer-feedback-2019.tsv"

# Variables
df_js = pd.read_json(BOT_DATASET_JSON_PATH)
df_tsv = pd.read_csv(BOT_DATASET_CSV_PATH, header = None, delim_whitespace = True)
#bot_id_list = []  # list of user IDs belonging to confirmed bots
#test_results_list = []  # list of test results
'''
BOT_DATASET_JSON_PATH = DIR_PATH + r"\gilani-2017_tweets.json"
BOT_DATASET_CSV_PATH = DIR_PATH + r"\gilani-2017.tsv"

# Variables
df_js = pd.read_json(BOT_DATASET_JSON_PATH)
df_tsv = pd.read_csv(BOT_DATASET_CSV_PATH, header = None, delim_whitespace = True)
'''

'''
how many times did having a profile pic lead to a bot or !bot

profile      |               P(bot)                 |             P(!bot)
=============+======================================+=====================================
hasProfile   |(hasProfilePic_withbot)/(total_bot)   | (hasProfilePic_with!bot)/(total_!bot)
=============+======================================+=====================================
hasntProfile |(hasntProfilePic_withbot)/(total_bot) | (hasntProfilePic_with!bot)/(total_!bot)

'''
#dictionary of dictionaries containing all the percentages needed
over_dict = {

    'total_bot_!bot': {
        "bot": 0.0,
        "!bot": 0.0
    },
    
    'name': {
        "hasName_bot": 0.0,
        "hasName_!bot": 0.0,
        "hasntName_bot": 0.0,
        "hasntName_!bot": 0.0
    },

    #Profile contains a bio (y, n)
    'bio': {
        "hasBio_bot": 0.0,
        "hasBio_!bot": 0.0,
        "hasntBio_bot": 0.0,
        "hasntBio_!bot": 0.0
    },
    
    #Follower count (0:100=0, 101:200=1, 201:300=2, 301:400=3, 401:500=4, 501:600=5, 601:700=6, 701:800=7, 801:900=8, beyond 900=9)
    'follower_int': {
        "0_bot": 0.0,
        "1_bot": 0.0,
        "2_bot": 0.0,
        "3_bot": 0.0,
        "4_bot": 0.0,
        "5_bot": 0.0,
        "6_bot": 0.0,
        "7_bot": 0.0,
        "8_bot": 0.0,
        "9_bot": 0.0,
        "0_!bot": 0.0,
        "1_!bot": 0.0,
        "2_!bot": 0.0,
        "3_!bot": 0.0,
        "4_!bot": 0.0,
        "5_!bot": 0.0,
        "6_!bot": 0.0,
        "7_!bot": 0.0,
        "8_!bot": 0.0,
        "9_!bot": 0.0
    },

    #Account has written at least 50 tweets (y, n)
    'min_tweets': {
        "has50tweets_bot": 0.0,
        "has50tweets_!bot": 0.0,
        "hasnt50tweets_bot":0.0,
        "hasnt50tweets_!bot": 0.0
    },
    
    #(2 * number of followers) >= (number of friends) (y, n)
    'follower_friend': {
        "hasmorefollower_bot": 0.0,
        "hasmorefollower_!bot":0.0,
        "hasntmorefollower_bot":0.0,
        "hasntmorefollower_!bot":0.0
        
    },
    
    #The bio does NOT contain the word “bot” (y,n)
    'contains_bot': {
        "hasbot_bot": 0.0,
        "hasbot_!bot": 0.0,
        "hasntbot_bot": 0.0,
        "hasntbot_!bot": 0.0
    },

    #Verified (y, n)
    'verified': {
        "isverified_bot": 0.0,
        "isverified_!bot": 0.0,
        "isntverified_bot": 0.0,
        "isntverified_!bot": 0.0
    },
    
    #Friend count (0:100=0, 101:200=1, 201:300=2, 301:400=3, 401:500=4, 501:600=5, 601:700=6, 701:800=7, 801:900=8, beyond 900=9)
    'friends_int': {
        "0_bot": 0.0,
        "1_bot": 0.0,
        "2_bot": 0.0,
        "3_bot": 0.0,
        "4_bot": 0.0,
        "5_bot": 0.0,
        "6_bot": 0.0,
        "7_bot": 0.0,
        "8_bot": 0.0,
        "9_bot": 0.0,
        "0_!bot": 0.0,
        "1_!bot": 0.0,
        "2_!bot": 0.0,
        "3_!bot": 0.0,
        "4_!bot": 0.0,
        "5_!bot": 0.0,
        "6_!bot": 0.0,
        "7_!bot": 0.0,
        "8_!bot": 0.0,
        "9_!bot": 0.0
    },
    
    #Default profile (T, F)
    'default' : {
        "hasdefaultprofile_bot": 0.0,
        "hasdefaultprofile_!bot": 0.0,
        "hasntdefaultprofile_bot": 0.0,
        "hasntdefaultprofile_!bot": 0.0
        
    },
    
    #Default profile (T, F)
    'notifications' : {
        "hasnotifications_bot": 0.0,
        "hasnotifications_!bot": 0.0,
        "hasntnotifications_bot": 0.0,
        "hasntnotifications_!bot": 0.0
        
    }
    
}

# Set results lists
def bot_results():
    results = []

    for index, row in df_tsv.iterrows():
        # If the user is a bot, add their twitter ID (row[0]) to the list
        if row[1] == "bot":
            results.append(row[0])

    return results


# Check if a user is a bot
def is_bot(id, id_list):
    bool = False

    if id in id_list:
        bool = True

    return bool


# Returns a list of dict, where the dict is the test results of the ith user
# Here is a legend for the keys in the dict:
#   "name"            : contains_name()
#   "bio"             : contains_bio()
#   "follower_int"    : followers_count_interval()
#   "min_tweets"      : minimum_tweets()
#   "follower_friend" : follower_friend_comparison()
#   "contains_bot"    : desc_not_contains_str()
#   "verified"        : is_verified()
#   "friends_int"     : friends_count_interval()
#   "default"         : is_default_profile()
#   "notifications"   : notifications_on()
#   "is_bot"          : is_bot()
def test_results():
    results = []

    for index, row in df_js.iterrows():
        results.append(run_tests(row))

    return results


# Run the battery of tests
def run_tests(row):
    my_bot_results = bot_results()

    dict = {
        "name" : contains_name(row["user"]["screen_name"], row["user"]["name"]),
        "bio" : contains_bio(row["user"]["description"]),
        "follower_int" : followers_count_interval(row["user"]["followers_count"]),
        "min_tweets" : minimum_tweets(row["user"]["statuses_count"]),
        "follower_friend" : follower_friend_comparison(row["user"]["followers_count"], row["user"]["friends_count"]),
        "contains_bot" : desc_not_contains_str(row["user"]["description"], "bot"),
        "verified" : is_verified(row["user"]["verified"]),
        "friends_int" : friends_count_interval(row["user"]["friends_count"]),
        "default" : is_default_profile(row["user"]["default_profile"]),
        "notifications" : notifications_on(row["user"]["notifications"]),
        "is_bot" : is_bot(row["user"]["id"], my_bot_results),
    }

    return dict


# Test rules implementation
def contains_name(screen_name, name):
    bool = False

    if screen_name != name:
        bool = True

    return bool


def contains_bio(desc):
    bool = False

    if desc != "":
        bool = True

    return bool


def followers_count_interval(count):
    val = -1

    if 0 <= count <= 100:
        val = 0
    elif 101 <= count <= 200:
        val = 1
    elif 201 <= count <= 300:
        val = 2
    elif 301 <= count <= 400:
        val = 3
    elif 401 <= count <= 500:
        val = 4
    elif 501 <= count <= 600:
        val = 5
    elif 601 <= count <= 700:
        val = 6
    elif 701 <= count <= 800:
        val = 7
    elif 801 <= count <= 900:
        val = 8
    elif count > 900:
        val = 9

    return val


def minimum_tweets(count):
    bool = False

    if count >= 50:
        bool = True

    return bool


def follower_friend_comparison(follow_count, friend_count):
    bool = False

    if (follow_count * 2) >= friend_count:
        bool = True

    return bool


def desc_not_contains_str(desc, str):
    bool = False

    if str in desc:
        bool = True

    return bool


def is_verified(bool):
    return bool


def friends_count_interval(count):
    val = -1

    if 0 <= count <= 100:
        val = 0
    elif 101 <= count <= 200:
        val = 1
    elif 201 <= count <= 300:
        val = 2
    elif 301 <= count <= 400:
        val = 3
    elif 401 <= count <= 500:
        val = 4
    elif 501 <= count <= 600:
        val = 5
    elif 601 <= count <= 700:
        val = 6
    elif 701 <= count <= 800:
        val = 7
    elif 801 <= count <= 900:
        val = 8
    elif count > 900:
        val = 9

    return val


def is_default_profile(bool):
    return bool


def notifications_on(bool):
    return bool

#

naive_data = []

yes_no_dict = []

tempy_dict = []
 
int_test = 0 #DEBUGING

def cnt_is_bot(data_dict):
    
    dict_val = "is_bot"
    
    temp_dict = {"tru": 0, "fals": 0}
    
    for val in data_dict:
        
        if (val.get(dict_val) == True):
            temp_dict["tru"] = temp_dict["tru"] + 1
        else:
            temp_dict["fals"] = temp_dict["fals"] + 1
        
    return (temp_dict)
    
'''
FUNCTION
cnt_perc: returns: dictionary
    

data_dict: type: dictionary
    should be the dictionary that we get from running test_results()

bot_nbot_dict: type: dictionary
    should be the total_yes_no dictionary from the list of dictionaries over_dict

dict_val: type: String
    should be the value in the dictionary one wants to extract

'''
def cnt_perc(data_dict, bot_nbot_dict, dict_val):
    
    ret_dict = {"bot_true": 0.0, "!bot_true": 0.0, "bot_false": 0.0, "!bot_false": 0.0}
    
    for val in data_dict:
        
        if(val.get("is_bot") == True): #for bots
            if(val.get(dict_val) == True):
                ret_dict["bot_true"] = ret_dict["bot_true"] + 1.0
            
            else:
                ret_dict["bot_false"] = ret_dict["bot_false"] + 1.0
            
        else: #for Humans
            if(val.get(dict_val) == True):
                ret_dict["!bot_true"] = ret_dict["!bot_true"] + 1.0
            
            else:
                ret_dict["!bot_false"] = ret_dict["!bot_false"] + 1.0
    
    #print(ret_dict) #DEBUGGING
    
    #is a bot and case was true 
    ret_dict["bot_true"] = ret_dict["bot_true"]/float(bot_nbot_dict["bot"])
    
    #is not a bot and case was true
    ret_dict["!bot_true"] = ret_dict["!bot_true"]/float(bot_nbot_dict["!bot"])
    
    #is a bot but case was not true
    ret_dict["bot_false"] = ret_dict["bot_false"]/float(bot_nbot_dict["bot"])
    
    #is not a bot and case was not true
    ret_dict["!bot_false"] = ret_dict["!bot_false"]/float(bot_nbot_dict["!bot"])
    
    return(ret_dict)
#cnt_perc ends here    

'''
FUNCTION
cnt_perc_num: returns: dictionary
    

data_dict: type: dictionary
    should be the dictionary that we get from running test_results()

bot_nbot_dict: type: dictionary
    should be the total_yes_no dictionary from the list of dictionaries over_dict

dict_val: type: String
    should be the value in the dictionary one wants to extract

'''
def cnt_perc_num(data_dict, bot_nbot_dict, dict_val):

    ret_dict = {
        "t0_bot": 0.0,
        "t1_bot": 0.0,
        "t2_bot": 0.0,
        "t3_bot": 0.0,
        "t4_bot": 0.0,
        "t5_bot": 0.0,
        "t6_bot": 0.0,
        "t7_bot": 0.0,
        "t8_bot": 0.0,
        "t9_bot": 0.0,
        "t0_!bot": 0.0,
        "t1_!bot": 0.0,
        "t2_!bot": 0.0,
        "t3_!bot": 0.0,
        "t4_!bot": 0.0,
        "t5_!bot": 0.0,
        "t6_!bot": 0.0,
        "t7_!bot": 0.0,
        "t8_!bot": 0.0,
        "t9_!bot": 0.0
    }
    
    for val in data_dict:
        if(val.get("is_bot") == True): #for bots
            if(val.get(dict_val) == 0):
                ret_dict["t0_bot"] = ret_dict["t0_bot"] + 1.0
            
            elif(val.get(dict_val) == 1):
                ret_dict["t1_bot"] = ret_dict["t1_bot"] + 1.0
            
            elif(val.get(dict_val) == 2):
                ret_dict["t2_bot"] = ret_dict["t2_bot"] + 1.0
            
            elif(val.get(dict_val) == 3):
                ret_dict["t3_bot"] = ret_dict["t3_bot"] + 1.0
            
            elif(val.get(dict_val) == 4):
                ret_dict["t4_bot"] = ret_dict["t4_bot"] + 1.0
            
            elif(val.get(dict_val) == 5):
                ret_dict["t5_bot"] = ret_dict["t5_bot"] + 1.0
            
            elif(val.get(dict_val) == 6):
                ret_dict["t6_bot"] = ret_dict["t6_bot"] + 1.0
            
            elif(val.get(dict_val) == 7):
                ret_dict["t7_bot"] = ret_dict["t7_bot"] + 1.0
            
            elif(val.get(dict_val) == 8):
                ret_dict["t8_bot"] = ret_dict["t8_bot"] + 1.0
            
            elif(val.get(dict_val) == 9):
                ret_dict["t9_bot"] = ret_dict["t9_bot"] + 1.0
                
            else:
                print("\nERROR in function cnt_perc_num in the is_bot section of the for loop\n")
                
        else: #for Humans (!bots)
            if(val.get(dict_val) == 0):
                ret_dict["t0_!bot"] = ret_dict["t0_!bot"] + 1.0
            
            elif(val.get(dict_val) == 1):
                ret_dict["t1_!bot"] = ret_dict["t1_!bot"] + 1.0
            
            elif(val.get(dict_val) == 2):
                ret_dict["t2_!bot"] = ret_dict["t2_!bot"] + 1.0
            
            elif(val.get(dict_val) == 3):
                ret_dict["t3_!bot"] = ret_dict["t3_!bot"] + 1.0
            
            elif(val.get(dict_val) == 4):
                ret_dict["t4_!bot"] = ret_dict["t4_!bot"] + 1.0
            
            elif(val.get(dict_val) == 5):
                ret_dict["t5_!bot"] = ret_dict["t5_!bot"] + 1.0
            
            elif(val.get(dict_val) == 6):
                ret_dict["t6_!bot"] = ret_dict["t6_!bot"] + 1.0
            
            elif(val.get(dict_val) == 7):
                ret_dict["t7_!bot"] = ret_dict["t7_!bot"] + 1.0
            
            elif(val.get(dict_val) == 8):
                ret_dict["t8_!bot"] = ret_dict["t8_!bot"] + 1.0
            
            elif(val.get(dict_val) == 9):
                ret_dict["t9_!bot"] = ret_dict["t9_!bot"] + 1.0
                
            else:
                print("\nERROR in function cnt_perc_num in the human section of the for loop\n")
            
    
    #print(ret_dict) #DEBUGGING
    
    #percentages for all the bots
    ret_dict["t0_bot"] = ret_dict["t0_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t1_bot"] = ret_dict["t1_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t2_bot"] = ret_dict["t2_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t3_bot"] = ret_dict["t3_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t4_bot"] = ret_dict["t4_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t5_bot"] = ret_dict["t5_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t6_bot"] = ret_dict["t6_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t7_bot"] = ret_dict["t7_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t8_bot"] = ret_dict["t8_bot"]/float(bot_nbot_dict["bot"])
    ret_dict["t9_bot"] = ret_dict["t9_bot"]/float(bot_nbot_dict["bot"])
    
    #percentages for all the !bots
    ret_dict["t0_!bot"] = ret_dict["t0_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t1_!bot"] = ret_dict["t1_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t2_!bot"] = ret_dict["t2_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t3_!bot"] = ret_dict["t3_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t4_!bot"] = ret_dict["t4_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t5_!bot"] = ret_dict["t5_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t6_!bot"] = ret_dict["t6_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t7_!bot"] = ret_dict["t7_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t8_!bot"] = ret_dict["t8_!bot"]/float(bot_nbot_dict["!bot"])
    ret_dict["t9_!bot"] = ret_dict["t9_!bot"]/float(bot_nbot_dict["!bot"])
    
    return(ret_dict)
#cnt_perc_num end here
    
#GETTING the percentages in naive bayes starts HERE
'''
For Botometer
total: 518
  are bots    are humans
{'tru': 139, 'fals': 379}

For Gilani
total: 2494

'''
naive_data = test_results()

print("\nNaive table dataset is done\n") #DEBUGGING

'''
for key in naive_data:
    #print(key, '\n')
    #print(key.get("follower_int"), '\n')
'''

tempy_dict = cnt_is_bot(naive_data)

over_dict['total_bot_!bot']['bot'] = tempy_dict['tru']
over_dict['total_bot_!bot']['!bot'] = tempy_dict['fals']

print(over_dict['total_bot_!bot'])

tempy_dict.clear()

#Calculates name column percentages
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "name")

over_dict['name']['hasName_bot'] = tempy_dict['bot_true']
over_dict['name']['hasName_!bot'] = tempy_dict['!bot_true']
over_dict['name']['hasntName_bot'] = tempy_dict['bot_false']
over_dict['name']['hasntName_!bot'] = tempy_dict['!bot_false']

print(over_dict['name']) #DEBUGGING

tempy_dict.clear()

#Calculates bio column percentages
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "bio")

over_dict['bio']['hasBio_bot'] = tempy_dict['bot_true']
over_dict['bio']['hasBio_!bot'] = tempy_dict['!bot_true']
over_dict['bio']['hasntBio_bot'] = tempy_dict['bot_false']
over_dict['bio']['hasntBio_!bot'] = tempy_dict['!bot_false']

print(over_dict['bio']) #DEBUGGING

tempy_dict.clear()

#Calculates follower_int percentages

tempy_dict = cnt_perc_num(naive_data, over_dict['total_bot_!bot'], "follower_int")

#Gives percentage value to follower_int dictionary
over_dict['follower_int']['0_bot'] = tempy_dict['t0_bot']
over_dict['follower_int']['1_bot'] = tempy_dict['t1_bot']
over_dict['follower_int']['2_bot'] = tempy_dict['t2_bot']
over_dict['follower_int']['3_bot'] = tempy_dict['t3_bot']
over_dict['follower_int']['4_bot'] = tempy_dict['t4_bot']
over_dict['follower_int']['5_bot'] = tempy_dict['t5_bot']
over_dict['follower_int']['6_bot'] = tempy_dict['t6_bot']
over_dict['follower_int']['7_bot'] = tempy_dict['t7_bot']
over_dict['follower_int']['8_bot'] = tempy_dict['t8_bot']
over_dict['follower_int']['9_bot'] = tempy_dict['t9_bot']
over_dict['follower_int']['0_!bot'] = tempy_dict['t0_!bot']
over_dict['follower_int']['1_!bot'] = tempy_dict['t1_!bot']
over_dict['follower_int']['2_!bot'] = tempy_dict['t2_!bot']
over_dict['follower_int']['3_!bot'] = tempy_dict['t3_!bot']
over_dict['follower_int']['4_!bot'] = tempy_dict['t4_!bot']
over_dict['follower_int']['5_!bot'] = tempy_dict['t5_!bot']
over_dict['follower_int']['6_!bot'] = tempy_dict['t6_!bot']
over_dict['follower_int']['7_!bot'] = tempy_dict['t7_!bot']
over_dict['follower_int']['8_!bot'] = tempy_dict['t8_!bot']
over_dict['follower_int']['9_!bot'] = tempy_dict['t9_!bot']


print(over_dict['follower_int']) #DEBUGGING

tempy_dict.clear()

#Calculates min_tweets column percentages
#note the has50tweets half only has 0's
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "min_tweet")

over_dict['min_tweets']['has50tweets_bot'] = tempy_dict['bot_true']
over_dict['min_tweets']['has50tweets_!bot'] = tempy_dict['!bot_true']
over_dict['min_tweets']['hasnt50tweets_bot'] = tempy_dict['bot_false']
over_dict['min_tweets']['hasnt50tweets_!bot'] = tempy_dict['!bot_false']

print(over_dict['min_tweets']) #DEBUGGING

tempy_dict.clear()

#Calculates follower_friend column percentages
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "follower_friend")

over_dict['follower_friend']['hasmorefollower_bot'] = tempy_dict['bot_true']
over_dict['follower_friend']['hasmorefollower_!bot'] = tempy_dict['!bot_true']
over_dict['follower_friend']['hasntmorefollower_bot'] = tempy_dict['bot_false']
over_dict['follower_friend']['hasntmorefollower_!bot'] = tempy_dict['!bot_false']

print(over_dict['follower_friend']) #DEBUGGING

tempy_dict.clear()

#Calculates contains_bot column percentages
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "contains_bot")

over_dict['contains_bot']['hasbot_bot'] = tempy_dict['bot_true']
over_dict['contains_bot']['hasbot_!bot'] = tempy_dict['!bot_true']
over_dict['contains_bot']['hasntbot_bot'] = tempy_dict['bot_false']
over_dict['contains_bot']['hasntbot_!bot'] = tempy_dict['!bot_false']

print(over_dict['contains_bot']) #DEBUGGING

tempy_dict.clear()

#Calculates verified column percentages 
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "verified")

over_dict['verified']['isverified_bot'] = tempy_dict['bot_true']
over_dict['verified']['isverified_!bot'] = tempy_dict['!bot_true']
over_dict['verified']['isntverified_bot'] = tempy_dict['bot_false']
over_dict['verified']['isntverified_!bot'] = tempy_dict['!bot_false']

print(over_dict['verified']) #DEBUGGING

tempy_dict.clear()

#Calculates friends_int percentages

tempy_dict = cnt_perc_num(naive_data, over_dict['total_bot_!bot'], "friends_int")

#Gives percentage value to follower_int dictionary
over_dict['friends_int']['0_bot'] = tempy_dict['t0_bot']
over_dict['friends_int']['1_bot'] = tempy_dict['t1_bot']
over_dict['friends_int']['2_bot'] = tempy_dict['t2_bot']
over_dict['friends_int']['3_bot'] = tempy_dict['t3_bot']
over_dict['friends_int']['4_bot'] = tempy_dict['t4_bot']
over_dict['friends_int']['5_bot'] = tempy_dict['t5_bot']
over_dict['friends_int']['6_bot'] = tempy_dict['t6_bot']
over_dict['friends_int']['7_bot'] = tempy_dict['t7_bot']
over_dict['friends_int']['8_bot'] = tempy_dict['t8_bot']
over_dict['friends_int']['9_bot'] = tempy_dict['t9_bot']
over_dict['friends_int']['0_!bot'] = tempy_dict['t0_!bot']
over_dict['friends_int']['1_!bot'] = tempy_dict['t1_!bot']
over_dict['friends_int']['2_!bot'] = tempy_dict['t2_!bot']
over_dict['friends_int']['3_!bot'] = tempy_dict['t3_!bot']
over_dict['friends_int']['4_!bot'] = tempy_dict['t4_!bot']
over_dict['friends_int']['5_!bot'] = tempy_dict['t5_!bot']
over_dict['friends_int']['6_!bot'] = tempy_dict['t6_!bot']
over_dict['friends_int']['7_!bot'] = tempy_dict['t7_!bot']
over_dict['friends_int']['8_!bot'] = tempy_dict['t8_!bot']
over_dict['friends_int']['9_!bot'] = tempy_dict['t9_!bot']


print(over_dict['friends_int']) #DEBUGGING

tempy_dict.clear()

#Calculates default column percentages
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "default")

over_dict['default']['hasdefaultprofile_bot'] = tempy_dict['bot_true']
over_dict['default']['hasdefaultprofile_!bot'] = tempy_dict['!bot_true']
over_dict['default']['hasntdefaultprofile_bot'] = tempy_dict['bot_false']
over_dict['default']['hasntdefaultprofile_!bot'] = tempy_dict['!bot_false']

print(over_dict['default']) #DEBUGGING

tempy_dict.clear()

#Calculates notifications column percentages
#Note: got the following results {'hasnotifications_bot': 0.0, 'hasnotifications_!bot': 0.0, 'hasntnotifications_bot': 1.0, 'hasntnotifications_!bot': 1.0}
tempy_dict = cnt_perc(naive_data, over_dict['total_bot_!bot'], "notifications")

over_dict['notifications']['hasnotifications_bot'] = tempy_dict['bot_true']
over_dict['notifications']['hasnotifications_!bot'] = tempy_dict['!bot_true']
over_dict['notifications']['hasntnotifications_bot'] = tempy_dict['bot_false']
over_dict['notifications']['hasntnotifications_!bot'] = tempy_dict['!bot_false']

print(over_dict['notifications']) #DEBUGGING

tempy_dict.clear()

naive_data.clear()

print("\nNaive table percentages is done\n") #DEBUGGING

BOT_DATASET_JSON_PATH = DIR_PATH + r"\botometer-feedback-2019_tweets.json"
BOT_DATASET_CSV_PATH = DIR_PATH + r"\botometer-feedback-2019.tsv"

df_js = pd.read_json(BOT_DATASET_JSON_PATH)
df_tsv = pd.read_csv(BOT_DATASET_CSV_PATH, header = None, delim_whitespace = True)


#print("\nBegin getting values for precision and recall tests\n") #DEBUGGING

#naive_data = test_results()


#print("\nDone with the the P&R dictionary now counting\n")



