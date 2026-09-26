numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# we have to pass even numbers in the list
# beginner
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)

# now using list comprehension
evens = [i for i in numbers if i % 2 == 0]
print(evens)
