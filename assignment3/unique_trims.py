import MapReduce
import sys

"""
Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id, a string representing a unique identifier for the sequence
    # value: nucleotides, a string representing a sequence of nucleotides
    key = record[0]
    value = record[1]
    trimmed = value[0:len(value)-10]
    mr.emit_intermediate(trimmed, 1)

def reducer(key, list_of_values):
    # key: trimmed nucleotides
    # value: list of occurrence counts
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
