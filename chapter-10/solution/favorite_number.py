from pathlib import Path
import json

favorite_number = input("Whats your favorite number? ")

contents = json.dumps(favorite_number)

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/favorite_numbers.json')

path.write_text(contents)