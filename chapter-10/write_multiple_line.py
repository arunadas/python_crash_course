from pathlib import Path

contents = "I love programming\n"
contents += "Its becoming cold\n"
contents += "Winter is here\n"
path = Path('/Users/prakash/Desktop/Aruna-learning/linkedin/python/python_crash_course/chapter-10/multipleLine_file.txt')
path.write_text(contents)