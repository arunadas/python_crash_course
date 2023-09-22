favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

for name , language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

print("\n")    

coders = ['jen','sarah','aruna','nupur']

for name in coders:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking poll")
    else:
        print(f"{name.title()}, you are invited to take language poll")    