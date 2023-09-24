favorite_places = {
    'suhel' : ['london', 'amritsar','paris'],
    'abhijeet' : ['france','russia','turkey'],
    'advaita':['turkey','delhi']
}

for name, places in favorite_places.items():
    print(f"{name.title()} likes the following places: ")
    for place in places:
        print(place)