def city_country(city, country):
    """print the formatted name of city and country"""
    city_country = f"{city}, {country}"

    return city_country.title()

city = city_country('fremont', 'usa')
print(city)

city = city_country('varanasi', 'india')
print(city)

city = city_country('delhi', 'india')
print(city)