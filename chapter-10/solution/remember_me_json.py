from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_username(path):
    """Prompt for a new username""" 
    user = {}
    username = input("What is your name? ")
    age = input("What is your age? ")
    location = input("What is your state? ")
    user['name'] = username
    user['age'] = age
    user['state'] = location
    contents = json.dumps(user)
    path.write_text(contents) 
    return user


def greet_user():
    """Greet the user bby name"""
    path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/username.json')
    user = get_stored_username(path)
    if user:
        print(f"Welcome back, {user}")
    else:
        user = get_new_username(path)
        print(f"We will remember you when you will come back, {user['name']}! of age {user['age']} who lives in {user['state']}")

greet_user()