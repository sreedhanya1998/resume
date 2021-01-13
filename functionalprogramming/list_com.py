# first=[1,2,3]
# second=[4,5,6]
f=[1,2,3,4,6,7]
# pairs=[(i,j) for i in first for j in second]
# print(pairs)
# #squares
# square=[i**2 for i in first]
# print(square)
#num-1 if num<5 else num+!
# data=[i-1 if i<5 else i+1 for i in f]
# print(data)
data=[i+1 if i>5 else i-1 if i<5 else 5 for i in f]
print(data)
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# flat=[j for i in matrix for j in i]
# print(flat)