student=["aman","chaman","bhaman"]
print("rahul" in student)

allowed_users=["admin","managers","staff"]
user=input("enter your role: ")
print(user in allowed_users)

blocked_user=["user1","user2"]
user_id=input("enter user id: ")
print(user_id not in blocked_user)
#if user 1 or 2 then false since we cant log in
