newf = open("output.txt")
goodf = open("tweet_sentiment_2.txt")

import json


def check(line):
  obj = json.loads(line)
  if obj.has_key("text") and obj.has_key("lang"):
    if obj["lang"] == "en":
      return line

for line in newf:
  x = check(line)
  if x:
    print x.strip()

#newsall = [check(line) for line in newf]
#news = [x for x in newsall if x][0:10]


#goods = [json.loads(line) for line in goodf]

#print goods

#for new, good in zip(news, goods):
#  new["text"] = good
#  print json.dumps(new)

