prompt = "Enter your age: "

age = input(prompt)
age = int(age)

if age < 3:
    print("your ticket is free ")
elif age >= 3 and age <= 12 :
    print(" your ticket price is $10 ")
else:
    print("yor ticket price is $15 ")        
