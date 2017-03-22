import sys
import json
import re

def getHash(fp):
	tweet_file = open(fp) #Open the file that contains tweets
	hash_list = []
	for tweet in tweet_file:
		decoded_tweet = json.loads(tweet) #Parse the data for every line in the tweet file.
		if "entities" in decoded_tweet : #Only retain lines that contain tweets,e.g. "text"
			entities = decoded_tweet["entities"]
			if 'hashtags' in entities:
			    hash = entities["hashtags"] #Select the hashtags of the tweet, as in a dictionary.
			    for hashT in hash:
			        h = hashT["text"].encode('utf-8')
			        hash_list.append(h) # Add each hash to the hash list
	return hash_list


def frequency(hash_list):
  hashDic = {} #Initiate a dictionary for all the hashtags
  total_count = 0
  for hash in hash_list: # for each hashtag selected above
	  total_count += 1 #Add one to the total count of hashtags
	  if hash in hashDic: #If the hashtag is in the dictionary
	    hashDic[hash] += 1 # Add one to the count for this hashtag in the dictionary
	  else : #If the hashtag is not in the dictionary
	    hashDic[hash] = 1 #Initiate the count for this hashtag in the dictionary	    

  freq = []
  for hash in hashDic:
    freq.append((hash, hashDic[hash]))
    freq = sorted(freq, key=lambda x: x[1], reverse = True)

  for i in range(10):
    print freq[i][0] + " " + str(float(freq[i][1]))


def main():  
    hash_list = getHash(sys.argv[1]) #Create the hash list
    frequency(hash_list) #Frequency each hash from the list

if __name__ == '__main__':
    main()