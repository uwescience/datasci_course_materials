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
    wordlist = {}
    for line in tweet_file:
      try:
          tweet = json.loads(line)['text']
      except:
#print 0
          continue
      tweet = re.findall('[\w]+',tweet)
      score = 0
      for word in tweet:
          if word not in wordlist:
              wordlist[word]=[1,1]
          try:
              score += scores[word]
          except:
              pass
      for word1 in tweet:
          if score > 0:
              wordlist[word1][0]+=1
          elif score < 0:
              wordlist[word1][1]+=1
    for word in wordlist:
        score = wordlist[word][0]/wordlist[word][1]
        print word,score
if __name__ == '__main__':
    main()
