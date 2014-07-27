import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of full-symmetric friend relationships for non-symmetric friend relationships.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    personA=record[0]
    personB=record[1]

    mr.emit_intermediate((personA, personB), 1)
    mr.emit_intermediate((personB, personA), -1)

def reducer(key, list_of_values):
    # key: the names of a pair of person name
    # value: list of 1
    total=0
    for v in list_of_values:
	total+=v

    if total!=0:
    	mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
