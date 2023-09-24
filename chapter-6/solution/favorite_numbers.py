favorite_number = {
    'Shandez' : [2,5],
    'Aruna' : [5,9,11,555],
    'Sarah' : [4,7,6],
    'Nelson' : [5,3,2],
    'Harish' : [1,0,7]
}

for name , numbers in favorite_number.items():
    print(f"{name.title()} has following favorite number")
    for number in numbers:
        print(number)