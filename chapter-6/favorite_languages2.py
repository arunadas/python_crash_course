favorite_languages = {
    'jen' : ['pyhton','rust'],
    'sarah' : ['c'],
    'edward' : ['rust','go'],
    'phil' : ['python','haskell']
}

for name , languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite langugages are:")
    for language in languages:
        print(f"\t {language.title()}")