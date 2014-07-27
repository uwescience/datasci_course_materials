import MapReduce
import sys

"""
mplement a relational join as a MapReduce query

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id

Your MapReduce query should produce the same result as this SQL query executed against an appropriate database. 
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: table_id(=line_item/order), list of attributes left 
    order_Id = record[1]  # order_id
    table_id = record[0]  # table_id
    attrs = record[1:]   # list of attributes left
    
    mr.emit_intermediate(order_Id, [table_id, attrs])
    

def reducer(key, list_of_values):
    # key: order_id
    # value: list of [table_id, attrs]
    order=[]
    line_Item=[]
    for v in list_of_values:
	if v[0]=="order":
	   order.append(v[1])
        else:
	   line_Item.append(v[1])

    for o in order:
	for l in line_Item:
	   mr.emit(["order"]+o+["line_item"]+l)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
