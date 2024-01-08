from pathlib import Path
import json

numbers = [2, 3, 5,7,11,13]

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)