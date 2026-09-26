import copy
a=[1,2,[3,4]]
b=copy.deepcopy(a)
b[2].append(5)
print(a)
print(b)