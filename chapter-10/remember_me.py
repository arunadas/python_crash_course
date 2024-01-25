from pathlib import Path
import json

username = input("What is your name? ")

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We will remember you when you will come back, {username}!")