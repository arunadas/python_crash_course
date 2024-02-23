from pathlib import Path
path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/solution/guest_book.txt')

contents = ''
while True:
    name = input("What is your name ? ")
    if name == 'quit':
        break
    
    contents += name + '\n'
    
path.write_text(contents)

