import sys
import json
from collections import Counter

encoding_type = "utf-8"
key = "text"


tags = []

def top10(tweet_file_name):

  tweet_file = open(tweet_file_name)
  for line in tweet_file:
    tweet_json = json.loads(line)
    
    if tweet_json.get('entities') and  tweet_json['entities'].get('hashtags') and tweet_json['entities']['hashtags']!=[]:
        for hashtag in tweet_json['entities']['hashtags']:
          tag = hashtag['text'].encode(encoding_type)
          tags.append(tag)
  tweet_file.close

def printTags():
  top = Counter(tags).most_common(10)
  for key,value in top:
    print key,float(value)

def main():
  tweet_file = sys.argv[1]
  top10(tweet_file)
  printTags()

if __name__ == '__main__':
  main()
