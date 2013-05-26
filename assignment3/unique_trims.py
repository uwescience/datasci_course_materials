import MapReduce
import sys

"""
Problem 5 - unique trims of dna
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence_id
    # value: nucleotides
    key = record[0]
    value = record[1]
    trimmed_nucleotides = value[0:len(value) - 10]
    mr.emit_intermediate(trimmed_nucleotides, 1)

def reducer(key, list_of_values):
    # key: trimmed_nucleotides
    # value: list of 1's which we'll ignore; we only want to return the unique trimmed nucleotides; which is done by MapReduce - the key is always unique
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
