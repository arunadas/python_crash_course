from pathlib import Path
import json

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/favorite_numbers.json')
contents = path.read_text()
favorite_number = json.dumps(contents)

print(favorite_number)