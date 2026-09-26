names=["aman","neha","ravi"]
for i in range(len(names)):
    print(i,names[i])

for index, name in enumerate(names):
    print(index,name) 
for index,name in enumerate(names,start=10):
    print(index,name)