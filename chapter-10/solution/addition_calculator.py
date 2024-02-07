print(f"Give me two number I will add them ")
print(f"Enter q for quitting")

while True:
    
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try :
        sum = int(first_number) + int(second_number)
    except ValueError:
        print(f" Please provide a integer value for addition")
    else:
        print(sum)        