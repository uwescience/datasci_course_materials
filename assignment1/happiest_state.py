import sys
import json
import re

States = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

States2 = {
        'Alaska':'AK',
        'Alabama':'AL',
        'Arkansas':'AR',
        'American Samoa':'AS',
        'Arizona':'AZ',
        'California':'CA',
        'Colorado':'CO',
        'Connecticut':'CT',
        'District of Columbia':'DC',
        'Delaware':'DE',
        'Florida':'FL',
        'Georgia':'GA',
        'Guam':'GU',
        'Hawaii':'HI',
        'Iowa':'IA',
        'Idaho':'ID',
        'Illinois':'IL',
        'Indiana':'IN',
        'Kansas':'KS',
        'Kentucky':'KY',
        'Louisiana':'LA',
        'Massachusetts':'MA',
        'Maryland':'MD',
        'Maine':'ME',
        'Michigan':'MI',
        'Minnesota':'MN',
        'Missouri':'MO',
        'Northern Mariana Islands':'MP',
        'Mississippi':'MS',
        'Montana':'MT',
        'National':'NA',
        'North Carolina':'NC',
        'North Dakota':'ND',
        'Nebraska':'NE',
        'New Hampshire':'NH',
        'New Jersey':'NJ',
        'New Mexico':'NM',
        'Nevada':'NV',
        'New York':'NY',
        'Ohio':'OH',
        'Oklahoma':'OK',
        'Oregon':'OR',
        'Pennsylvania':'PA',
        'Puerto Rico':'PR',
        'Rhode Island':'RI',
        'South Carolina':'SC',
        'South Dakota':'SD',
        'Tennessee':'TN',
        'Texas':'TX',
        'Utah':'UT',
        'Virginia':'VA',
        'Virgin Islands':'VI',
        'Vermont':'VT',
        'Washington':'WA',
        'Wisconsin':'WI',
        'West Virginia':'WV',
        'Wyoming' :'WY'
}

def dict(fn):
	sent_file = open(fn)
	scores = {} # initialize an empty dictionary
	for line in sent_file:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	return scores 

def getTweet(fp):
	tweet_file = open(fp) #Open the file that contains tweets
	tweet_dic = {}
	for tweet in tweet_file:
		decoded_tweet = json.loads(tweet) #Parse the data for every line in the tweet file.
		if "place" in decoded_tweet:
		  place = decoded_tweet["place"]
		  if place is not None:
		    if place["country_code"] == "US":
		      if place["full_name"] is not None :
		        state0 = place["full_name"].split(",")[1].split()[0].encode('utf-8')
		        state1 = place["full_name"].split(",")[0].split()[0].encode('utf-8')     
		        if state0 in States or state1 in States.values():
		          if state0 in States:
		            state = state0
		          else:
		            state = States2[state1]
		          if "text" in decoded_tweet : #Only retain lines that contain tweets,e.g. "text"
			        text = decoded_tweet["text"].encode('utf-8') #Select the text of the tweet, as in a dictionary, and encode to get proper international characters.
			        tweet_dic[text] = state # Add each text to the tweet list
	return tweet_dic


def sent(score_list, tweet_dic):
	state_score = {}
	for tweet in tweet_dic: # for each tweet selected above
		tweet_score = 0 #Set the starting score to 0
		tweet_words = re.findall(r"[\w']+",tweet,re.IGNORECASE) #Split each tweet to retain only the words
		
		for word in tweet_words: #For each word selected
			if word in score_list: #If the word is in the sentiment file dictionary
				word_score = score_list[word] # get the word score from this dictionary
			else : #If the word is not in the dictionary
				word_score = 0 #Put the score of this word to 0
			tweet_score += word_score #Sum scores of each word to get a total tweet score
		if tweet_dic[tweet] in state_score:
		    state_score[tweet_dic[tweet]] += tweet_score
		else:
		    state_score[tweet_dic[tweet]] = tweet_score
	
	# finding the state with the max score
	v = list(state_score.values())
	k = list(state_score.keys())
	print k[v.index(max(v))]

def main():  
    scores = dict(sys.argv[1]) #Create the dictionary from the sentiment file
    tweet_list = getTweet(sys.argv[2]) #Create the tweet list
    sent(scores, tweet_list) #Score each tweet from the list

if __name__ == '__main__':
    main()
