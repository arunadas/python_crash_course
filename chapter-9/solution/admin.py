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

class Admin(User):
    """Model admin """ 

    def __init__(self, first, last, age, country):
        super().__init__(first, last, age, country)
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can update user'] 

    def show_privileges(self):
        """print the admin privileges""" 
        [print(privilege) for privilege in self.privileges]         



