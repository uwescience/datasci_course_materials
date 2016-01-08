import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    
    tweet_file.readline()
    for line in tweet_file:
      obj = json.loads(line)
      if "text" in obj:
        tweet = obj[u"text"]
        score = 0
        for word in tweet.split():
          if word in scores:
            score += scores[word]        
        print score  


if __name__ == '__main__':
    main()
