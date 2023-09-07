usernames = ['john', 'admin', 'aruna','priya','shandiz']

for username in usernames :
    if username == 'admin':
        print("Hello admin, would you like a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again ")    