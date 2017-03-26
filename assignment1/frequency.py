import sys
import json

def count_freq(data, dictionary, total_count):
	words = data.split()
	for word in words:
		if word in dictionary:
			dictionary[word] = dictionary[word] + 1
		else:
			dictionary[word] = 1
	total_count += len(words)
	return (dictionary, total_count)


def parse_tweet_file(tweet_file):
	# one line is one tweet
		# retrieve the text from the tweet
		# call the method to calculate frequencies
		# 
	freq = {}
	total = 0
	
	for tweet_line in tweet_file:
		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			freq, total = count_freq(tweet_json['text'], freq, total)
	
	return (freq, total)

def calc_word_frequencies(word_counts, total_word_count):
	word_freqs = {}
	for word_pair in word_counts.items():
		#print type(word_pair)
		#print word_pair
		word = word_pair[0]
		word_count = word_pair[1]
		#print word_count
		#print total_word_count
		word_frequency = float(word_count) / float(total_word_count)
		#print "word: %s freq: %s"%(word, word_frequency)
		word_freqs[word] = word_frequency
	return word_freqs

def main():
	tweet_file = open(sys.argv[1])
	word_counts, total_word_count = parse_tweet_file(tweet_file)
	#print word_counts
	#print total_word_count
	
	word_frequencies = calc_word_frequencies(word_counts, total_word_count)
	
	for term_freq in word_frequencies.items():
		print "%s %s"%(term_freq[0].encode('utf-8'), str(term_freq[1]))
	
if __name__ == '__main__':
	main()