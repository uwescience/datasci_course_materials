import sys
import re

import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
#import pdb;pdb.set_trace()
    for line in tweet_file:
      try:
          tweet = json.loads(line)['text']
      except:
          print 0
          continue
      tweet = re.findall('[\w]+',tweet)
      score = 0
      for word in tweet:
          try:
              score += scores[word]
          except:
              pass
      print score

if __name__ == '__main__':
    main()
