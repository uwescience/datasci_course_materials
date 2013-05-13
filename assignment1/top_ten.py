import sys
import json
from operator import itemgetter, attrgetter

def count_hashtags(tweet_file):
	hashtag_counts = {}
	
	for tweet_line in tweet_file:
		tweet_json = json.loads(tweet_line)
		#print tweet_json['created_at']
		if 'entities' in tweet_json:
			if 'hashtags' in tweet_json['entities']:
				for hashtag_item in tweet_json['entities']['hashtags']:
					#print hashtag_item
					if 'text' in hashtag_item:
						if hashtag_item['text'] in hashtag_counts:
							hashtag = hashtag_item['text']
							hashtag_counts[hashtag] += 1
						else:
							hashtag = hashtag_item['text']
							hashtag_counts[hashtag] = 1
	
	return hashtag_counts
	
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
	tweet_file = open(sys.argv[1])
	hashtag_counts = count_hashtags(tweet_file)
	#print word_counts
	#print total_word_count
	
	topTen = 10
	top_ten_hashtags = take_topX_hashtags(hashtag_counts, topTen)
	
	for hashtag_data in top_ten_hashtags:
		print "%s %s"%(hashtag_data[0].encode('utf-8'), str(float(hashtag_data[1])))
	
if __name__ == '__main__':
	main()