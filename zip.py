names = ["aman", "neha", "ravi"]
marks = [80, 90, 70]
for i in range(len(names)):
    print(names[i], marks[i])
for name, mark in zip(names, marks):
    print(name, mark)
# if the marks list is [80,90] there will be only two pairs as for
# for loop it will give index out of the range problem or issue
