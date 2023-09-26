pets = []

pet_0 = {
    'type':'Dog',
    'owner':'paul'
}

pets.append(pet_0)

pet_1 = {
    'type':'Cat',
    'owner':'suhel'
}

pets.append(pet_1)

pet_2 = {
    'type':'squirrel',
    'owner':'advaita'
}

pets.append(pet_2)

pet_3 = {
    'type':'mouse',
    'owner':'sandip'
}

pets.append(pet_3)

pet_4 = {
    'type':'lizard',
    'owner':'abhijeet'
}

pets.append(pet_4)

for pet in pets:
    for key , value in pet.items():
        print(f"\t{key} : {value}")
        