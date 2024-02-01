from pathlib import Path


def count_word(path, filename):
    try :
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
       # print(f"Sorry, the file {filename} does not exist. ") 
       pass
    else:
        # count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")   

filenames = ['alice.txt', 'moby_dick.txt','little_women.txt', 'siddhartha.txt']

for filename in filenames:
    path = Path(f"/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/{filename}")
    count_word(path, filename)