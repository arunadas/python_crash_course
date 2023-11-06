def make_car(manufacturer, model, **cars_info):
    """Build a car dictionary with the info provided"""
    cars_info['manufacturer'] = manufacturer
    cars_info['model name'] = model
    return cars_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
