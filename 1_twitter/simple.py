import json
tweetfile = open("output.txt")
for line in tweetfile:
  obj = json.loads(line)
  print obj
  raw_input() # to pause the program until a key is pressed
