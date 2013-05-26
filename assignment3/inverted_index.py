import MapReduce
import sys

"""
Problem 1 - inverted index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    document_id = record[0]
    document_contents = record[1]
    words = document_contents.split()
    for w in words:
      mr.emit_intermediate(w, document_id)

def reducer(key, list_of_values):
    # key: word
    # value: list of document_ids
    document_list = []
    for v in list_of_values:
      if v not in document_list:
         document_list.append(v) # try to remove the duplicate document ids; if the word is found in the document multiple times
    mr.emit((key, document_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
