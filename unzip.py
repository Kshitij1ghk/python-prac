# unzip is a concept not a function or method
data = [("aman", 80), ("neha", 90), ("ravi", 70)]
names, marks = zip(*data)
print(names)
print(marks)
# the output is in tuple
'''datas=[1,2,3,4,5]
data1,data2=zip(*datas)
print(data1)
print(data2) gives error since unzip needs pairs or multiple iterables'''
