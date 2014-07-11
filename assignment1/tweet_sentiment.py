import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_setscore_dict(score_fp):
    scores = {} # initialize an empty dictionary
    score_list = []
    
    for line in score_fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term.lower()] = int(score)  # Convert the score to an integer.
        #if term.find(" ")>0:
        #    print term
        
    #print scores.items() # Print every (term, score) pair in the dictionary
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
       
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    #sent_file.seek(0)
    #tweet_file.seek(0)
    # create the (term, score) pair dictionary 
    score_dict = get_setscore_dict(sent_file)
    
    # calculator the score for nth lines in the file
    for line in tweet_file:
        data = json.loads(line)
        if data.has_key('text'):
            text = data['text'].encode('utf-8')
            #print text
            line_score = cal_score(text, score_dict)
            print line_score
        else:
            print 0

if __name__ == '__main__':
    main()
