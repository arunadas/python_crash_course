def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)

def make_pizza(*toppings):
    """Summarizing the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green pappers', 'extra cheese')  

def make_pizza2(size, *toppings):
    """Summarizing the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza2(16, 'pepperoni')
make_pizza2(12,'mushrooms', 'green pappers', 'extra cheese')         
