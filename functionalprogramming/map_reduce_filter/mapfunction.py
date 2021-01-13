lst=[10,11,12,13,14,15]

# def squares(no):
# #     return no**2
# square=list(map(squares,lst))
# print(square)
square=list(map(lambda no:no**2,lst))
print(square)
cubes=list(map(lambda no:no**3,lst))
print(cubes)