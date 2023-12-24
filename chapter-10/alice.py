from pathlib import Path

path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/alice.txt')
try :
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist. ") 
else:
    # count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file alice.txt has about {num_words} words")       