class Restaurant:
    """Model restaurent"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attribute"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"restaurant name is {self.restaurant_name}")  
        print(f"restaurant cuisine is {self.cuisine_type}")  

    def open_restaurant(self):
        """States whether restaurant is open"""
        print(f"This restaurant is open")

class IceCreamStand(Restaurant):
    """Model ice cream stand"""

    def __init__(self,restaurant_name, cuisine_type):
        """Initialize ice cream stand and flavors"""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['strawberry','cherry','lichi']

    def describe_flavors(self):
        """Print the flavors of the iceCream"""
        [print(i) for i in self.flavors]  

ponny = IceCreamStand('ponny','ice cream')
ponny.describe_flavors()
