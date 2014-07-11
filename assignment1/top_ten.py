import sys
import json

def main():
    tweet_file = open(sys.argv[1])

    # dict[term:count]
    tag_dict = {}
    cnt=0

    # get the text in the entities.hashtags and state the count
    for line in tweet_file:
        data = json.loads(line)
        if data.has_key('entities') and type(data['entities'])!=type(None) and data['entities'].has_key('hashtags') and type(data['entities']['hashtags'])!=type(None):
            hashtags = data['entities']['hashtags']
	    
	    for ht in hashtags:
		text = ht['text'].encode('utf-8').lower()
		tag_dict[text] = tag_dict.get(text, 0) + 1
		cnt += 1

   # sort the tag
    sort_tag = sorted(tag_dict.items(), key=lambda e:e[1], reverse=True)
    for idx in range(0,10):
    	print str(sort_tag[idx][0])+' '+str(sort_tag[idx][1])

   

if __name__ == '__main__':
    main()
