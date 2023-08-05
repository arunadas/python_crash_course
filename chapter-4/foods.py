my_foods= ['pizza', 'falafel','carrot cake']
# make a copy using splice
friends_food = my_foods[:]
my_foods.append('chat')
friends_food.append('sushi')

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite food are:")
print(friends_food)

# assignment = makes a reference to same list
friends_food2 = my_foods 

my_foods.append('chicken tikka masala')
friends_food2.append('Ghee roast')

print("My favorite food are:")
print(my_foods)

print("\nMy friend's favorite food are:")
print(friends_food2)

print("My favorite food are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite food are:")
for food in friends_food2:
    print(food)    

