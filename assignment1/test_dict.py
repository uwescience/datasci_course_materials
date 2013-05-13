s = "george ivanov george python"
s2 = "ivanov radi learning python"

def count_freq(data, dictionary, total_count):
	words = data.split()
	for word in words:
		if word in dictionary:
			dictionary[word] = dictionary[word] + 1
		else:
			dictionary[word] = 1
	total_count += len(words)
	print data
	print dictionary
	print total_count
	return (dictionary, total_count)

dict = {}
total_count = 0
dict, total_count = count_freq(s, dict, total_count)
dict, total_count = count_freq(s2, dict, total_count)
