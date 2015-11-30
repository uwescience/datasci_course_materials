import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0] == "a":
        for k in range(0,5,1):
            mr.emit_intermediate((record[1],k), record)
    if record[0] == "b":
        for k in range(0,5,1):
            mr.emit_intermediate((k,record[2]), record)   

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #print key, list_of_values
    a = [0] * 5
    b = [0] * 5
    for l in list_of_values:
        if l[0] == "a":
            a[l[2]] = l[3]
        if l[0] == "b":   
            b[l[1]] = l[3]
        result = sum([i*j for i,j in zip(a,b)])
    value = (key[0], key[1], result)
    mr.emit(value)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
