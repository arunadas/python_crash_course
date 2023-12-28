from pathlib import Path


path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/pi_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
for line in lines:
    print(line)

