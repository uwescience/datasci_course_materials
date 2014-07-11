import sys
import json

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


def get_setscore_dict(score_fp):
    scores = {} # initialize an empty dictionary
    score_list = []
    
    for line in score_fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term.lower()] = int(score)  # Convert the score to an integer.

    return scores

def cal_score(text, score_dict):
    sum = 0
    span = 3 # the max length phrase is 2
    
    text_words = text.lower().split()
    word_cnt =  len(text_words)
    idx = 0
    while idx<word_cnt:
        for pos in range(span,0,-1):
            sublist = text_words[idx:idx+pos]
            term = str(' '.join(sublist))
            # find the key
            if score_dict.has_key(term):
                sum += score_dict[term]
                break
        # end of for
        
        if pos==0:
            idx+=1
        else:
            idx += pos
    # end of while

    return sum

def find_state(state_name):
   sn = state_name.strip(' ')
   if len(sn)>2:
   	# state_name is longger than abbr
   	for s in states.keys():
     	   if states[s] in sn:
	   	return s

   return sn

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # create the (term, score) pair dictionary 
    score_dict = get_setscore_dict(sent_file)
    state_score={}

    for line in tweet_file:
        data = json.loads(line)

        if data.has_key('text'):
            text = data['text'].encode('utf-8')
            line_score = cal_score(text, score_dict)

	    if data.has_key('place') and type(data['place'])!=type(None):
		p = data['place']
		if p['country']!='United States':
		   continue

		if p.has_key('full_name'):
	   	    pname = p['full_name'].split(',')
		    if 'USA' in pname[1]:
		        state_name=pname[0]
		    else:
		        state_name=pname[1]

		    state_abbr = find_state(state_name)
	    	    state_score[state_abbr]=state_score.get(state_abbr,0)+line_score

    max_score=-1
    happiest_state=''
    for s in state_score.keys():
	if state_score[s] > max_score:
	   happiest_state = s
	   max_score = state_score[s]

    print happiest_state

if __name__ == '__main__':
    main()

