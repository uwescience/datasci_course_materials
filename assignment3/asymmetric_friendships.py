import MapReduce
import sys

"""
Problem 4 - the relationship symmetric problem
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: personA
    # value: personB
    key = record[0]
    value = record[1]
    words = value.split()
    # we emit the original friend pair with value 1, and the symmetric one with value -1; if there corresponding input pair with the symetric values, then the sum with the same key will be 0; if only input, there will be only 1
    mr.emit_intermediate((key, value), 1)
    mr.emit_intermediate((value, key), -1)

def reducer(key, list_of_values):
    # key: (personA, personB)
    # value: list of values - (1) or (-1)
    personA = key[0]
    personB = key[1]
    input_pair = (1 in list_of_values)
    reverse_pair = (-1 in list_of_values)
    if (input_pair & reverse_pair == False):
        mr.emit((personA, personB))
        #mr.emit((personB, personA))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
