import sys
import json
import re

def getTweet(fp):
	tweet_file = open(fp) #Open the file that contains tweets
	tweet_list = []
	for tweet in tweet_file:
		decoded_tweet = json.loads(tweet) #Parse the data for every line in the tweet file.
		if "text" in decoded_tweet : #Only retain lines that contain tweets,e.g. "text"
			text = decoded_tweet["text"].encode('utf-8') #Select the text of the tweet, as in a dictionary, and encode to get proper international characters.
			tweet_list.append(text) # Add each text to the tweet list
	return tweet_list


def frequency(tweet_list):
  wordsDic = {} #Initiate a dictionary for all the words
  total_count = 0
  for tweet in tweet_list: # for each tweet selected above
    tweet_words = re.findall(r"[\w']+",tweet,re.IGNORECASE) #Split each tweet to retain only the words
		
    for word in tweet_words: #For each word selected
	  total_count += 1 #Add one to the total count of words
	  if word in wordsDic: #If the word is in the dictionary
	    wordsDic[word] += 1 # Add one to the count for this word in the dictionary
	  else : #If the word is not in the dictionary
	    wordsDic[word] = 1 #Initiate the count for this word in the dictionary	    

  for word in wordsDic:
    wordsDic[word] = float(wordsDic[word]) / float(total_count)
    print word + " " + str("%.5f" % round(wordsDic[word],5))
	  

def main():  
    tweet_list = getTweet(sys.argv[1]) #Create the tweet list
    frequency(tweet_list) #Score each tweet from the list

if __name__ == '__main__':
    main()