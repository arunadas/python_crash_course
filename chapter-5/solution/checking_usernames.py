current_users = ['John', 'JEnny', 'aruna','Priya','shandiz']
current_users_lower = [user.lower() for user in current_users]

new_users = ['JOHN', 'jenny', 'tom','andy','monty']

for user in new_users:
    if user.lower() in current_users_lower:
        print("Already in use, please choose another username")
    else:
        print("Added new user")




