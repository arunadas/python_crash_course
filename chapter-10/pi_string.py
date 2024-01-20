from pathlib import Path


path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/pi_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))    

