from pathlib import Path

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/learning_python.txt')

contents = path.read_text().strip()
print(contents)