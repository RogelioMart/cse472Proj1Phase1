import json
'''
dict_perc.json: dictionary of percentages used to calculate naive bayes (used the gilani-2017_tweets.json file to make it )

naive_dict.json: dictionary used to test the naive dataset
'''

'''
NBC_binary: returns dictionary

@param
row: dictionary
   takes in 1 row from a dictionary
   
percentage: dictionary
    The nested dictionary used to to calculate a bot percentage
    (The one Rogelio made)
    
sKey: string
    key for the column that is currently being computed.
    
hasX_Bot: string
    key for the discrete data

hasX_nBot: string
    key for the discrete data

hasntX_Bot: string
    key for the discrete data

hasntX_nBot: string
    key for the discrete data
    
'''
def NBC_binary(row, percentages, sKey, hasX_Bot, hasX_nBot, hasntX_Bot, hasntX_nBot):
    
    ret_dict = {"ret_Bot": 0.0, "ret_nBot": 0.0}
    
    if(row.get(sKey) == True):
            
        ret_dict["ret_Bot"] = percentages[sKey][hasX_Bot]
            
        ret_dict["ret_nBot"] = percentages[sKey][hasX_nBot]
        
    else: #row.get(sKey) == False
        
        ret_dict["ret_Bot"] = percentages[sKey][hasntX_Bot]
            
        ret_dict["ret_nBot"] = percentages[sKey][hasntX_nBot]
        
    return(ret_dict)

'''
NBC_binary: returns dictionary

@param
row: dictionary
   takes in 1 row from a dictionary
   
percentage: dictionary
    The nested dictionary used to to calculate a bot percentage
    (The one Rogelio made)

identifier: string
    The key used to get the proper percentage from the column
'''
def NBC_10(row, percentages, identifier):
    
    ret_dict = {"ret_Bot": 0.0, "ret_nBot": 0.0}
    
    #print("\nNum is " + str(row.get(identifier)) + "\n")

    
    if(row.get(identifier) == 0):
        ret_dict["ret_Bot"] = percentages[identifier]["0_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["0_!bot"]
    elif(row.get(identifier) == 1):
        ret_dict["ret_Bot"] = percentages[identifier]["1_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["1_!bot"]
    elif(row.get(identifier) == 2):
        ret_dict["ret_Bot"] = percentages[identifier]["2_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["2_!bot"]
    elif(row.get(identifier) == 3):
        ret_dict["ret_Bot"] = percentages[identifier]["3_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["3_!bot"]
    elif(row.get(identifier) == 4):
        ret_dict["ret_Bot"] = percentages[identifier]["4_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["4_!bot"]
    elif(row.get(identifier) == 5):
        ret_dict["ret_Bot"] = percentages[identifier]["5_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["5_!bot"]
    elif(row.get(identifier) == 6):
        ret_dict["ret_Bot"] = percentages[identifier]["6_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["6_!bot"]
    elif(row.get(identifier) == 7):
        ret_dict["ret_Bot"] = percentages[identifier]["7_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["7_!bot"]
    elif(row.get(identifier) == 8):
        ret_dict["ret_Bot"] = percentages[identifier]["8_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["8_!bot"]
    elif(row.get(identifier) == 9):
        ret_dict["ret_Bot"] = percentages[identifier]["9_bot"]
        ret_dict["ret_nBot"] = percentages[identifier]["9_!bot"]
    else:
        print("\nERROR in the NBC_10 with " + identifier)
        
    #print("end of func")
    
    #print(ret_dict)
    
    return(ret_dict)

def NBC_math(row, overall_dict):

    '''
    name2_dict = {
        "dos": {"main": "bio","hasX_Bot_t": "hasBio_bot", "hasX_nBot_t": "hasBio_!bot", "hasntX_Bot_t": "hasntBio_bot", "hasntX_nBot_t": "hasntBio_!bot"},
        "cinco": {"main": "follower_friend", "hasX_Bot_t": "hasmorefollower_bot", "hasX_nBot_t": "hasmorefollower_!bot", "hasntX_Bot_t": "hasntmorefollower_bot", "hasntX_nBot_t": "hasntmorefollower_!bot"},
        "seis":{"main": "contains_bot", "hasX_Bot_t": "hasbot_bot", "hasX_nBot_t": "hasbot_!bot", "hasntX_Bot_t": "hasntbot_bot", "hasntX_nBot_t": "hasntbot_!bot"},
        "siete":{"main": "verified", "hasX_Bot_t": "isverified_bot", "hasX_nBot_t": "isverified_!bot", "hasntX_Bot_t": "isntverified_bot", "hasntX_nBot_t": "isntverified_!bot"},
        "nueve":{"main": "default", "hasX_Bot_t": "hasdefaultprofile_bot", "hasX_nBot_t": "hasdefaultprofile_!bot", "hasntX_Bot_t": "hasntdefaultprofile_bot", "hasntX_nBot_t": "hasntdefaultprofile_!bot"}
    }
    
    "cuatro": {"main": "min_tweet", "hasX_Bot_t": "has50tweets_bot", "hasX_nBot_t": "has50tweets_!bot", "hasntX_Bot_t": "hasnt50tweets_bot", "hasntX_nBot_t": "hasnt50tweets_!bot"}
    "diez": {"main": "notifications", "hasX_Bot_t": "hasnotifications_bot", "hasX_nBot_t": "hasnotifications_!bot", "hasntX_Bot_t": "hasntnotifications_bot", "hasntX_nBot_t": "hasntnotifications_!bot"}
    '''
    ret_dict = {"ret_Bot": 0.0, "ret_nBot": 0.0, "true_val": True}
    
    hold_dict = []
    
    Bot_str = ""
    nBot_str = ""
    
    #name
    hold_dict = NBC_binary(key, overall_dict, "name", "hasName_bot", "hasName_!bot", "hasntName_bot", "hasntName_!bot")
    
    ret_dict["ret_Bot"] = hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #bio
    hold_dict = NBC_binary(key, overall_dict, "bio", "hasBio_bot", "hasBio_!bot", "hasntBio_bot", "hasntBio_!bot")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #follower_int
    hold_dict = NBC_10(key, overall_dict, "follower_int")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #follower_friend
    hold_dict = NBC_binary(key, overall_dict, "follower_friend", "hasmorefollower_bot", "hasmorefollower_!bot", "hasntmorefollower_bot", "hasntmorefollower_!bot")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #contain_bot
    hold_dict = NBC_binary(key, overall_dict, "contains_bot", "hasntbot_bot", "hasntbot_!bot" ,"hasbot_bot", "hasbot_!bot")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #verified
    hold_dict = NBC_binary(key, overall_dict, "verified", "isverified_bot", "isverified_!bot", "isntverified_bot", "isntverified_!bot")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #friend_int
    hold_dict = NBC_10(key, overall_dict, "friends_int")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #default
    hold_dict = NBC_binary(key, overall_dict, "default", "hasdefaultprofile_bot", "hasdefaultprofile_!bot", "hasntdefaultprofile_bot", "hasntdefaultprofile_!bot")
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * hold_dict["ret_Bot"]
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * hold_dict["ret_nBot"]
    
    Bot_str = Bot_str + str(hold_dict["ret_Bot"]) + "*"
    nBot_str = nBot_str + str(hold_dict["ret_nBot"]) + "*"
    
    hold_dict.clear()
    
    #ret_dict = {"ret_Bot": 0.0, "ret_nBot": 0.0, "true_val": ''}
    
    ret_dict["true_val"] = key["is_bot"]
    
    ret_dict["ret_Bot"] = ret_dict["ret_Bot"] * (1090/2494) #(overall_dict["total_bot_!bot"]["bot"]/(overall_dict["total_bot_!bot"]["bot"] + overall_dict["total_bot_!bot"]["!bot"]))
    
    ret_dict["ret_nBot"] = ret_dict["ret_nBot"] * (1404/2494)#(overall_dict["total_bot_!bot"]["!bot"]/(overall_dict["total_bot_!bot"]["bot"] + overall_dict["total_bot_!bot"]["!bot"]))
    
    #print(Bot_str + '\n\n') #
    
    #print(nBot_str + '\n')
    
    return(ret_dict)

def bot_or_not(decide_dict):

    #ret_dict = {"ret_Bot": 0.0, "ret_nBot": 0.0, "true_val": True}
    
    #only needs TP FP FN
    
    ret_str = ""
    
    if(decide_dict["ret_Bot"] > decide_dict["ret_nBot"]):#it is a bot (positive)
        
        if(decide_dict["true_val"] == True): #TP
            ret_str = "TP"
        else: #FP
            ret_str = "FP"
            
    elif( decide_dict["ret_Bot"] < decide_dict["ret_nBot"]): # it is not a bot (negative)
        
        if(decide_dict["true_val"] == False): #TN
            ret_str = "TN"
        else: #FN
            ret_str = "FN"
    else: #Undecided UN
        ret_str = "UN"
        
    return(ret_str)
    
        
        
def data_analysis(tp, fp, tn, fn, un):

    precision = 0
    recall = 0
    tprecision = 0.0
    trecall = 0.0
    fmeasure = 0.0
    accuracy = 0
    tot_wrong = 0
    
    accuracy = round(((tp + tn)/(tp + fp + tn + fn + un)), 5)
    #tot_wrong = round(((fp + fn)/(tp + fp + tn + fn + un)), 2) * 100
    
    tprecision = tp/(tp + fp)
    trecall = tp/(tp + fn)
    
    fmeasure = round(2 *((tprecision * trecall)/(tprecision + trecall)), 5)
    
    precision = round((tp/(tp + fp)), 5)
    recall = round((tp/(tp + fn)), 5)
    
    print("True Postive: " + str(tp) + "\n\n")
    print("False Postive: " + str(fp) + "\n\n")
    print("True Negative: " + str(tn) + "\n\n")
    print("False Negative: " + str(fn) + "\n\n")
    print("Unknown: " + str(un) + "\n\n")
    
    print("Accuracy: " + str(accuracy) + "\n\n")
    #print("Percentage of incorrect Guesses: " + str(tot_wrong) + "%\n\n")
    print("Precision: " + str(precision) + "\n\n")
    print("Recall: " + str(recall) + "\n\n")
    print("F Measure: " + str(fmeasure) + "\n\n")
    
    return(0)
    
    
    
    

print("\nThis program tests the implementation model for naive bayes classifier by calculating metrics.\n\n")

trueP = 0
falseP = 0
trueN = 0
falseN = 0
unknown = 0 #If this one is counted that means they tied.

cnt = 0

with open('dict_perc.json') as f:
    overall_dict = json.load(f)
    
f.close()

with open('naive_dict.json') as g:
    P_R_dict = json.load(g)
    
g.close()

temp_dict = []

pre_decide = ""



for key in P_R_dict:

    #temp_dict = NBC_binary(key, overall_dict, "name", "hasName_bot", "hasName_!bot", "hasntName_bot", "hasntName_!bot")
    #temp_dict = NBC_binary(key, overall_dict, "bio", "hasBio_bot", "hasBio_!bot", "hasntBio_bot", "hasntBio_!bot")
    #temp_dict = NBC_10(key, overall_dict, "follower_int")
    
    temp_dict = NBC_math(key, overall_dict)
    
    pre_decide = bot_or_not(temp_dict)
    
    if(pre_decide == "TP"):
        trueP = trueP + 1
    
    elif(pre_decide == "FP"):
        falseP = falseP + 1
    
    elif(pre_decide == "TN"):
        trueN = trueN + 1
    
    elif(pre_decide == "FN"):
        falseN = falseN + 1
    
    elif(pre_decide == "UN"):
        unknown = unknown + 1
    
    else:
        print("ERROR: WHEN DECIDED PRECISION AND RECALL SOMETHING WENT WRONG")
    
    #print(temp_dict)
    #print("\n\n")
    temp_dict.clear()


data_analysis(trueP, falseP, trueN, falseN, unknown)

''' 
for n_id, n_info in overall_dict.items():

    print("\nColumn: ", n_id)
    
    for key in n_info:
        print('   ' + key + ':', n_info[key])


   
for key3 in P_R_dict:
    #print(key3, '\n')
    #for key5 in key3:
    #    print(key5, '\n')
    cnt = cnt + 1
    
print(str(cnt))
'''



