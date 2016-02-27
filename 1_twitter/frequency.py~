import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    
    lines = tweet_file.readlines()

    tweets = []
    for (i, line) in enumerate(lines):
      obj = json.loads(line)
      if "text" in obj and "lang" in obj:
        if obj["lang"] != "en": continue
        tweet = obj[u"text"]
        score = 0
        for word in tweet.split():
          if word in scores:
            score += scores[word]        
        tweets.append((obj, score))

    terms = {}
    termcount = 0
    for (tweet, score) in tweets:
      for word in tweet["text"].split():
        termcount += 1
        terms[word] = terms.setdefault(word, 0.0) + 1

    
    ss = sorted([(score/termcount, t) for (t,score) in terms.items()])
    for s,t in ss:
      print s, t

      


if __name__ == '__main__':
    main()
