import sys
import json

def clean_text_word(words_list):
    word_cnt =  len(words_list)
    new_list = []
    
    for i in range(0,word_cnt):
        if not words_list[i].startswith("@") and not words_list[i].startswith("http"):
            new_word = filter(str.isalpha, words_list[i])
            if len(new_word)>0:
                new_list.append(new_word)

    return new_list

def main():
    tweet_file = open(sys.argv[1])

    # dict[term:count]
    word_dict = {}
    cnt=0

    # calculator the score for nth lines in the file
    for line in tweet_file:
        data = json.loads(line)
        if data.has_key('text'):
            text = data['text'].encode('utf-8').lower()
	    words_list = clean_text_word(text.split())
		
            for w in words_list:
	    	word_dict[w]=word_dict.get(w, 0)+1.0
		cnt += 1.0

    for w in word_dict:
        print w+" "+"%.4f" % (word_dict[w]/cnt)


if __name__ == '__main__':
    main()
