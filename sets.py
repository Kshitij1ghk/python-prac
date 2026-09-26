emails = {"kshitij@gmai.com", "kshitij@gmai.com",
          "kolej@gmai.com", "kaster@gmai.com", "sandali@gmai.com"}
print(emails)

num = [1, 2, 3, 4, 4, 4, 1, 2, 3, 4, 5,]
s = set(num)
print("unique: ", s)  # same for converting a tuple to set

a = {1, "A", (2, 3), (2, 3)}
print(a)

'''x={[1,2]}
print(X) gives error'''

b = {1, 2, 3, 5, 5, 6}
b.add(7)
b.discard(5)
print(b)

# combine multiple unique values
m = {1, 2, 3}
n = {3, 4, 5}
print(m | n)  # this is called union

# to find common values
print(m & n)

# to find extra or differece
print(m-n)


# frozen set
fs = frozenset([1, 2, 3, 4, 5, 4, 5, 6, 6])
print(fs)
# fs.add(4) gives error
