import sys import json import operator

states = {
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

encoding_type = "utf-8"
key = "text"

scores = {} # initialize an empty dictionary
happy_candidates = {}

def loadScores(sent_file):
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

def findHappyState(tweet_file):
    
  for line in tweet_file:
    tweet_json = json.loads(line)
    score = 0 
    if tweet_json.get('text') and tweet_json.get('place') and tweet_json['place']['country_code']=='US':
      tweet = tweet_json[key].encode('utf-8').split()
      for word in tweet:
        score += float(scores.get(word,0))
  
      state = tweet_json['place']['full_name'].encode('utf-8')[-2:]
      
      if state in states.keys():
        if state not in happy_candidates:
          happy_candidates[state] = score
        else:
          happy_candidates[state] += score
  
  if len(happy_candidates)>0:
    print max(happy_candidates.iteritems(),key=operator.itemgetter(1))[0]
  #print max(happy_candidates,key=happy_candidates.get)
  
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    loadScores(sent_file)
    findHappyState(tweet_file)

if __name__ == '__main__':
    main()
