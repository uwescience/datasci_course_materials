import MapReduce
import sys

"""
compute the matrix multiplication A x B
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #input: [matrix, i, j, value] 
    # key: [i,j]
    # value: A/B[i,j]
    a_nrow=5
    b_ncol=5
    matrix=record[0]
    i=record[1]
    j=record[2]
    value=record[3]

    if matrix=="a":
	for k in range(0,b_ncol):
	   mr.emit_intermediate((i,k), (matrix,j,value))
    else:  # matrix=="b"
    	for k in range(0,a_nrow):
      	   mr.emit_intermediate((k,j), (matrix,i,value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    a_matrix={}
    b_matrix={}
    for v in list_of_values:
      if  v[0]=="a":
	a_matrix[v[1]]=v[2]
      else:
	b_matrix[v[1]]=v[2]

    for k in range(0,5):
	total+=a_matrix.get(k,0)*b_matrix.get(k,0)

    mr.emit((key[0], key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
