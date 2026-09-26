numbers=[1,2,3,4,5,6]
# we need to see squares of each numbers in list
#beginner
square=[]
for i in numbers:
    square.append(i*i)
print(square)

#for this python gives list comprehension
squares=[i*i for i in numbers]
print(squares)
#[new value for iten in list] for list comprehension