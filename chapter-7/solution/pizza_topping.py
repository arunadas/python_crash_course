prompt = "Enter the topping you want "
prompt += "(Enter quit to close)"

active = True
while active:

    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(topping)