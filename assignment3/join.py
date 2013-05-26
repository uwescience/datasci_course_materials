import MapReduce
import sys

"""
Problem 2 - join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # index 0 is the table name - line_item or order, index 1 is the order_id
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_records):
    # key: order_id
    # value: list of records - must be two items otherwise skip
    #print list_of_records
    #print key
    order_record = ''
    for record in list_of_records:
       if record[0] == 'order':
           order_record = record
    
    #order_record = order_record[1:10]

    #print order_record

    if (order_record != ''):
       for record1 in list_of_records:
           if record1[0] == 'line_item':
              line_item_record = record1  #[1:17]
              joined_relation = []
              for i in order_record:
                  joined_relation.append(i)
              for i in line_item_record:
                  joined_relation.append(i)

              #print line_item_record
              #print len(joined_relation)
              #print order_record + line_item_record
              mr.emit(joined_relation)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
