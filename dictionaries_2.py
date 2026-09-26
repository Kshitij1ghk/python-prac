x = {
    "a": [1, 2, 3],
    "a": [10, 20, 30]  # overwrites ffirst one
}
print(x)

student = {}

student["id"] = 101
student["name"] = "kshitij"
student["age"] = 22
student["marks"] = 98

print(student)

student.update({
    "city": "delhi",
    "grade": "A"
})
print(student["name"])

# to access keys only
print(student.keys())
print(student.values())

#using loops on dictionary to access we use items
for key, value in student.items():
    print(key, ":", value)


#update
"""student["id"]=102 one method"""
#can use update to change values too 
#delete
student.pop("age")
print(student)
#better than delete since it will not give error if key not present
#and will only give empty results