from random import randint
class Die:
    """Model die"""

    def __init__(self, sides=6):
        """Initialize the die """
        self.sides = sides

    def roll_die(self):
        """print a random roll dice"""
        return randint(1, self.sides) 

d6 = Die()
results = []
for i in range(10):
    roll = d6.roll_die() 
    results.append(roll)    

print("10 rolls of a 6-sided die:")
print(results)          

d10 = Die(sides=10)
print(f"10 die")
print("10",d10.sides)
results = []
for i in range(10):
    roll = d10.roll_die()
    results.append(roll)
print("\n10 rolls of a 10-sided die:")
print(results)     

d20 = Die(sides=20)
print(f"20 die")
print("20",d20.sides)
results = []
for i in range(10):
    roll = d20.roll_die() 
    results.append(roll) 
print("\n10 rolls of a 20-sided die:")
print(results)       