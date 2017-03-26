afinnfile = open("AFINN-111.txt")
scores = {} # initialize an empty dictionary

for line in afinnfile:
    term, score = line.split("\t") # each line is tab del
    scores[term] = int(score) # convert the score to int
	
print scores.items() # prints every term, score pairs