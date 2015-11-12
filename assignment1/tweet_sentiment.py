import sys
import json
import re

def dict(fn):
	sent_file = open(fn)
	scores = {} # initialize an empty dictionary
	for line in sent_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	return scores 

def getTweet(fp):
	tweet_file = open(fp) #Open the file that contains tweets
	tweet_list = []
	for tweet in tweet_file:
		decoded_tweet = json.loads(tweet) #Parse the data for every line in the tweet file.
		if "text" in decoded_tweet : #Only retain lines that contain tweets,e.g. "text"
			text = decoded_tweet["text"].encode('utf-8') #Select the text of the tweet, as in a dictionary, and encode to get proper international characters.
			tweet_list.append(text) # Add each text to the tweet list
	return tweet_list


def sent(score_list, tweet_list):
	for tweet in tweet_list: # for each tweet selected above
		tweet_score = 0 #Set the starting score to 0
		tweet_words = re.findall(r"[\w']+",tweet,re.IGNORECASE) #Split each tweet to retain only the words
		
		for word in tweet_words: #For each word selected
			if word in score_list: #If the word is in the sentiment file dictionary
				word_score = score_list[word] # get the word score from this dictionary
			else : #If the word is not in the dictionary
				word_score = 0 #Put the score of this word to 0
			tweet_score += word_score #Sum scores of each word to get a total tweet score
		print float(tweet_score)

def main():  
    scores = dict(sys.argv[1]) #Create the dictionary from the sentiment file
    tweet_list = getTweet(sys.argv[2]) #Create the tweet list
    sent(scores, tweet_list) #Score each tweet from the list

if __name__ == '__main__':
    main()
