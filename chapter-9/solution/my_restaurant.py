from restaurent import Restaurant
restaurant = Restaurant('Taz','Indian')
print(f"My restaurant name is {restaurant.restaurant_name}")
print(f"My restaurant  serves {restaurant.cuisine_type} cuisine")   

restaurant.describe_restaurant()
restaurant.open_restaurant()