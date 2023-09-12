favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language} .")

# using get 

alien_0 = {'color' : 'green', 'speed':'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

print("\n")
for name , language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
print("\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")  
print("\n")    
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")      
print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

print("\n")
print(f" Following languages have been mentioned") 
for languages in favorite_languages.values():
    print(languages.title())   

# use of set to list only unique values
print(f" Following unique languages have been mentioned") 
for languages in set(favorite_languages.values()):
    print(languages.title())    