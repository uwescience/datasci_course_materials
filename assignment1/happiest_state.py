import sys
import json
from operator import itemgetter, attrgetter

def find_single_sentiment_in_text(sentiment_data, text):
	total_sentiment = 0.0
	term = sentiment_data[0]
	score = sentiment_data[1]
	term_count = text.count(term)
	total_sentiment = term_count * score
	# print "total_sentiment: %s, term: %s, score: %s, count: %s"%(str(total_sentiment), term, str(score), str(term_count))
	return total_sentiment
	
def parse_tweet_state(tweet_json):
	tweet_state = ''
	if 'place' in tweet_json and tweet_json['place']:
		if 'country' in tweet_json['place'] and tweet_json['place']['country']:
			#print tweet_json['place']['country']
			if tweet_json['place']['country'].lower() == 'united states':
				if 'full_name' in tweet_json['place']:
					city, state = tweet_json['place']['full_name'].split(',')
					tweet_state = state.strip().upper()
	#print tweet_state
	return tweet_state

def calc_state_sentiment(scores, tweet_file):
	state_sentiment = {}
	idx = 0
	for tweet_line in tweet_file:
		tweet_sentiment = 0.0
		#print tweet_line
		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			tweet_text = tweet_json['text'].encode('utf-8') 
			tweet_sentiment = find_single_sentiment_in_text(scores[idx], tweet_text)		
		#result_sentiments.append(tweet_sentiment)
		#print tweet_sentiment
		
		tweet_state = parse_tweet_state(tweet_json)
		if tweet_state != '':
			if tweet_state in state_sentiment:
				state_sentiment[tweet_state] += tweet_sentiment
			else:
				state_sentiment[tweet_state] = tweet_sentiment
				
		idx += 1
		
	return state_sentiment
	
def build_sent_dict(afinnfile_path):
    afinnfile = open(afinnfile_path)
    scores = []
    for i, line in enumerate(afinnfile):
		term, score = line.split("\t") # each line is tab del
		scores.append((term, int(score))) # convert the score to int
    return scores
	
def take_topX_hashtags(hashtag_counts, top_count):
	# convert the dict to set
	# sort the set using the 2nd item in the tuple in descending order
	hashtag_counts = sorted(hashtag_counts.iteritems(), key=itemgetter(1), reverse=True)
	
	#print hashtag_counts

	# select the top X items from the newly sorted set
	top_x_items = []
	i = 0
	for hashtag_item in hashtag_counts:
		if (i < top_count):
			top_x_items.append(hashtag_item)
			i += 1
		else:
			break
	
	return top_x_items

	
def main():
	scores = build_sent_dict(sys.argv[1])
	tweet_file = open(sys.argv[2])
	state_sentiment = calc_state_sentiment(scores, tweet_file)

	# print state_sentiment
	
	top_state = take_topX_hashtags(state_sentiment, 1)
	
	if len(top_state) > 0:
		print top_state[0][0] 
	
if __name__ == '__main__':
    main()
