import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_setscore_dict(score_fp):
    scores = {} # initialize an empty dictionary
    
    for line in score_fp:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term.lower()] = int(score)  # Convert the score to an integer.
        #if term.find(" ")>0:
        #    print term
        
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def clean_text_word(words_list):
    word_cnt =  len(words_list)
    new_list = []
    
    for i in range(0,word_cnt):
        if not words_list[i].startswith("@") and not words_list[i].startswith("http"):
            new_word = filter(str.isalpha, words_list[i])
            if len(new_word)>0:
                new_list.append(new_word)

    return new_list
               
def cal_score(text, score_dict, nolevel_list):
    sum = 0
    span = 3 # the max length phrase is 2

    text_words = text.lower().split()
    text_words = clean_text_word(text_words)

    word_cnt =  len(text_words)
    idx = 0
    new_word = []
    
    while idx<word_cnt:
        for pos in range(span,0,-1):
            sublist = text_words[idx:idx+pos]
            term = str(' '.join(sublist))
            # find the key
            if score_dict.has_key(term):
                sum += score_dict[term]
                break
        # end of for

        if pos==1:
            no_sent_word = text_words[idx]
            idx += 1
            if not nolevel_list.has_key(no_sent_word):
                new_word.append(no_sent_word)
        else:
            idx += pos
    # end of while
    return [sum, new_word]
    
def stat_w(sum_score, word_stat):
    stat={}
    if len(word_stat)>0:
            stat['total_cnt'] = word_stat['total_cnt'] + 1
            stat['sum'] = word_stat['sum'] + sum_score
    else:
            stat['total_cnt']=1
            stat['sum'] = sum_score

    return stat
             

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
     
    #sent_file = open("AFINN-111.txt")
    #tweet_file = open("problem_1_submission.txt")

    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    # create the (term, score) pair dictionary 
    score_dict = get_setscore_dict(sent_file)

    # dict[key, sum, total_cnt]
    word_to_sent = {}
    new_words=[]
    
    # calculator the score for nth lines in the file
    for line in tweet_file:
        data = json.loads(line)
        if data.has_key('text'):
            text = data['text'].encode('utf-8')
            #print text
            score_nolevel_word = cal_score(text, score_dict, word_to_sent)
            sum = score_nolevel_word[0]  # sentiment of line
            new_words = score_nolevel_word[1]   # no sentiment word appear in the line
            
            for w in new_words:
                word_to_sent[w] = stat_w(sum, word_to_sent.get(w,{}) )
                
        
    # cal sentiment at last
    for word in word_to_sent.keys():
        new_score = word_to_sent[word]['sum']/word_to_sent[word]['total_cnt']
        print word+" "+str(new_score)

if __name__ == '__main__':
    main()
