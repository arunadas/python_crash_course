from user import User

class Privileges:
    """Defining privilege class"""

    def __init__(self, privileges=[]):
        """Initialize the privilege class"""
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can update user']   

    def show_privileges(self):
        """print the admin privileges""" 
        [print(privilege) for privilege in self.privileges]          

class Admin(User):
    """Model admin """ 

    def __init__(self, first, last, age, country):
        super().__init__(first, last, age, country)
        self.privilege = Privileges()