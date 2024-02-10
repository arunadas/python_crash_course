from pathlib import Path

filenames = ['theBigFour.txt', 'theWasteLand.txt']

def read_files(filename):
    path = Path(filename)
    return path.read_text(encoding='utf-8')

def count_words(contents, word):
    lines = contents.splitlines()
    #print(lines)
    word_counts = 0
    for line in lines:
        word_counts += line.lower().count(word)
    return word_counts    

word = input("What the word you want to count? ")

for filename in filenames:
    try:
        contents = read_files(f"/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/{filename}")
    except FileNotFoundError:
        print(f"{filename} does not exist")
    else:     
        if word == 'q':
            break   
       # word = "the"
        count = count_words(contents, word)
        print(f"The number of count for {word} in {filename} is {count}")



