from pathlib import Path

filenames = ['cats.txt', 'dog.txt']

def read_files(filename):
    path = Path(filename)
    return path.read_text()

for filename in filenames:

    try:
        contents = read_files(f"/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/{filename}")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    else:
        print(contents)



