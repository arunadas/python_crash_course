def build_person(first_name, last_name):
    "Return dictionary of information about a person"
    person = {'first':first_name, 'last':last_name}
    return person

musician = build_person('Michael','jackson')
print(musician)


def build_person(first_name, last_name, age=None):
    "Return dictionary of information about a person"
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Michael','jackson', age=35)
print(musician)