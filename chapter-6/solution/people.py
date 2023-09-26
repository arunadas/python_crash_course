people = []
person_0 = {
    'first_name' : 'jhonny',
    'last_name' : 'lee',
    'age' : 35 ,
    'city' : 'sanfrancisco'
}
people.append(person_0)

person_1 = {
    'first_name' : 'Pavan',
    'last_name' : 'Mitra',
    'age' : 25 ,
    'city' : 'varanasi'
}
people.append(person_1)

person_2 = {
    'first_name' : 'zubin',
    'last_name' : 'zaharia',
    'age' : 45 ,
    'city' : 'paris'
}
people.append(person_2)

people = [person_0 , person_1, person_2]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}  is {person['city']}, lives in {person['first_name'].title()}")