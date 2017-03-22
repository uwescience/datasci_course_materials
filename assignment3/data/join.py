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
    table = record[0]
    order = record[1]
    value = [record[0],record]
    mr.emit_intermediate(order, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    for val in list_of_values:
        result = list(list_of_values[0][1])
        if val[0] == "line_item":
            for v in val[1]:
                result.append(v)            
            mr.emit(result)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)