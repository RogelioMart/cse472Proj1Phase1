# read_retweets.py

# libraries
import tweepy

# local modules
import config

import networkx as nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt

import collections

MENTIONS_GRAPH = nx.Graph()

# authorization variables
auth = tweepy.OAuthHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# get mentions
def recursion(screen_name, counter, max_depth, mentions, tweets, file_ptr, graph):
    
    if counter < max_depth:
    
        counter += 1
        mention_count = 0
        
        tempUser = api.get_user(screen_name)
        
        if(tempUser.protected == False):
        
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
                        print_to_file(screen_name, first_mention, file_ptr, graph)
                        
                        # call recursion on first mention
                        recursion(first_mention, counter, max_depth, mentions, tweets, file_ptr, graph)


# print the mentions to a log file
def print_to_file(user_name, mention_name, file_ptr, graph):
    file_ptr = open(config.EDGE_LOG_PATH, "a")
    file_ptr.write(user_name + " " + mention_name + "\n")
    file_ptr.close()
    graph.add_edge(user_name, mention_name)
    
    
def main():
    
    file_ptr = open("edge_file.txt", "w")
    file_ptr.write("")
    file_ptr.close()
    
    recursion("HIDEO_KOJIMA_EN", 0, 5, 4, 10, file_ptr, MENTIONS_GRAPH)
    
    #Returns the number of nodes that were plotted
    print("Number of Nodes: " + str(MENTIONS_GRAPH.number_of_nodes()) + "\n")
    
    #Draws the node graph for the acquired nodes
    nx.draw(MENTIONS_GRAPH, with_labels = True)
    plt.savefig("mentions_graph.png")

    #Does the network distribution and draws it
    degree_sequence = sorted([d for n, d in MENTIONS_GRAPH.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")

    plt.title("Degree Histogram")
    plt.ylabel("Count")
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)

    # draw graph in inset
    plt.axes([0.4, 0.4, 0.5, 0.5])
    Gcc = MENTIONS_GRAPH.subgraph(sorted(nx.connected_components(MENTIONS_GRAPH), key=len, reverse=True)[0])
    pos = nx.spring_layout(MENTIONS_GRAPH)
    plt.axis("off")
    plt.show()
    
    #calculates and displays the Diameter of the graph
    print( "\nDiameter(basically the maxiumum eccentricity): "+ str(nx.networkx.algorithms.distance_measures.diameter(MENTIONS_GRAPH)))

    #calculates and displays the reciprocity of the graph
    print("\nreciprocity" + str(nx.overall_reciprocity(MENTIONS_GRAPH)))
    
    
    
    
main()