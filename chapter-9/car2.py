class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make , model , year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly descriptive name."""
        long_name = f"{self.year} {self.make} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement to show car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    
my_new_car = Car('audi','a4', 2024)
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()  

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()
