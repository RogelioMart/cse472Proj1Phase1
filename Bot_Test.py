# Bot_Test.py
# Dataset: botometer-feedback-2019
#   direct download: (https://botometer.osome.iu.edu/bot-repository/datasets/botometer-feedback-2019/botometer-feedback-2019.tar.gz)
#   source: https://botometer.osome.iu.edu/bot-repository/datasets.html


# libraries
import pandas as pd
import os

# local modules
import config


# Constants
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
BOT_DATASET_JSON_PATH = DIR_PATH + r"\botometer-feedback-2019_tweets.json"
BOT_DATASET_CSV_PATH = DIR_PATH + r"\botometer-feedback-2019.tsv"

# Variables
df_js = pd.read_json(BOT_DATASET_JSON_PATH)
df_tsv = pd.read_csv(BOT_DATASET_CSV_PATH, header = None, delim_whitespace = True)
#bot_id_list = []  # list of user IDs belonging to confirmed bots
#test_results_list = []  # list of test results


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
        "is_bot" : is_bot(row["id"], my_bot_results),
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
