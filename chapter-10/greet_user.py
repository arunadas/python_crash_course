from pathlib import Path
import json

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}")