first_number = input("First number: ")
second_number = input("Second number: ")

try :
    sum = int(first_number) + int(second_number)
except ValueError:
    print(f" Please provide a integer value for addition")
else:
    print(sum)        