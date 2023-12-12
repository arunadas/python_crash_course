class User:
    """Model users"""

    def __init__(self, first, last, age, country):
        """Initialize attributes of user"""
        self.first_name = first.title()
        self.last_name = last.title()
        self.age = age
        self.country = country.title()
        self.login_attempts = 0

    def describe_user(self):
        """Summarize user's information"""
        print(f"\nUser name is {self.first_name} {self.last_name}")
        print(f"Age is {self.age} and lives in {self.country} country")

    def greet_user(self):
        """greeting message to the user"""
        print(f"{self.first_name} {self.last_name} you are welcome here")

    def increment_login_attempts(self):
        """Add 1 to the login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attemt as 0"""
        self.login_attempts = 0        

aruna = User('aruna', 'das', 40, 'USA')        
   
aruna.describe_user()
aruna.greet_user()

for i in range(5):
    aruna.increment_login_attempts()

print(aruna.login_attempts)

aruna.reset_login_attempts()
print(f" after reset {aruna.login_attempts}")