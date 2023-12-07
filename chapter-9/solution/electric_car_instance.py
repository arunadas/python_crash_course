class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make , model , year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement to show car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back"""
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't revert back an odometer!")    

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """Model battery for electric car."""

    def __init__(self, battery_size = 40):
        """Initialize the battery's attributes """
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")   

    def upgrade_battery(self):
        """Upgrade the battery size to 65 after checking it. """

        if self.battery_size == 40 :
            self.battery_size = 65
            print(f"Upgraded the battery to 65 kwh")
        else:
            print(f"The battery is already upgraded")    


    def get_range(self):
        "What is the range of this battery"
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")              

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

       

my_leaf = ElectricCar('nissan','leaf', 2024)
print(my_leaf.get_descriptive_name()) 
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

