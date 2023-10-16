sandwich_orders = ['tuna sandwich', 'pastrami','turkey sandwich','pastrami', 'veggi sandwich','pastrami']

print("Deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"your {current_sandwich} is made")
    finished_sandwiches.append(current_sandwich)

for finish_sandwich in finished_sandwiches:
    print(finish_sandwich.title())     