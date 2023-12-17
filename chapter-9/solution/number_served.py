class Restaurant:
    """Model restaurent"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attribute"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"restaurant name is {self.restaurant_name}")  
        print(f"restaurant cuisine is {self.cuisine_type}")  

    def open_restaurant(self):
        """States whether restaurant is open"""
        print(f"This restaurant is open")

    def customer_served(self):
        """Number of customer served"""
        print(f"Customer server at this restaurent {self.number_served}")   

    def set_number_served(self, customers):
        """Update the customer served"""
        self.number_served = customers  

    def increment_number_served(self, customers):
        self.number_served += customers       

restaurant = Restaurant('Taz','Indian')   

restaurant.describe_restaurant()
restaurant.customer_served()

restaurant.number_served = 50
restaurant.customer_served()

restaurant.set_number_served(100)
restaurant.customer_served()

restaurant.increment_number_served(10)
restaurant.customer_served()