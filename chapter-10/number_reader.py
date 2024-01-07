from pathlib import Path
import json

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)