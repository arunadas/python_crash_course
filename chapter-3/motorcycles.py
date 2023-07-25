motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducanti'
print(motorcycles)

motorcycles.append('kawasaki')
print(motorcycles)

# inserting to element at index
motorcycles.insert(0,'honda')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I own was {first_owned.title()}")
motorcycles.append('ducanti')
motorcycles.append('enfield')

motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'ducanti'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")