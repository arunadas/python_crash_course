name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

age = input("How old you are? ")
age = int(age)
print(f"\n Your age , {age}")
if age >= 18 :
    print(age)
