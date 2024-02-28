from pathlib import Path
path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/guest.txt')
name = input("What is your name ? ")

path.write_text(name)

