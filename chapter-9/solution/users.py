class User:
    """Model users"""

    def __init__(self, first, last, age, country):
        """Initialize attributes of user"""
        self.first_name = first.title()
        self.last_name = last.title()
        self.age = age
        self.country = country.title()

    def describe_user(self):
        """Summarize user's information"""
        print(f"\nUser name is {self.first_name} {self.last_name}")
        print(f"Age is {self.age} and lives in {self.country} country")

    def greet_user(self):
        """greeting message to the user"""
        print(f"{self.first_name} {self.last_name} you are welcome here")

aruna = User('aruna', 'das', 40, 'USA')        
johney = User('jhoney', 'deph', 56, 'USA')
yaksha = User('yaksha', 'lo', 30, 'Japan')    

aruna.describe_user()
aruna.greet_user()

johney.describe_user()
johney.greet_user()

yaksha.describe_user()
yaksha.greet_user()