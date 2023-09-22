cities = {
    'varanasi' : {
        'country': 'india',
        'population' : 1789047,
        'fact': 'has ganga'

    },
    'london' : {
        'country': 'united kingdom',
        'population' : 9648000,
        'fact': 'over 300 languages spoken in london'

    },
    'sanfrancisco' : {
        'country': 'USA',
        'population' : 715717,
        'fact': 'has sea lions in pier 39'

    }
}

for city, city_details in cities.items():
    country = city_details['country']
    population = city_details['population']
    fact = city_details['fact']
    
    print(f"{city.title()} is in {country}")
    print(f" this has population of {population}")
    print(f" this has fun fact as {fact}")

