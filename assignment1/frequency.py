import sys
import re

import json

def main():
    tweet_file = open(sys.argv[1])
#import pdb;pdb.set_trace()
    wordlist = {}
    for line in tweet_file:
      try:
          tweet = json.loads(line)['text']
      except:
#print 0
          continue
      tweet = re.findall('[\w]+',tweet)
      for word in tweet:
          if word not in wordlist:
              wordlist[word]=1
          else:
              wordlist[word]+=1
    total = sum(wordlist.values())
    for word in wordlist:
        score = float(wordlist[word])/total
        print word,score
if __name__ == '__main__':
    main()
