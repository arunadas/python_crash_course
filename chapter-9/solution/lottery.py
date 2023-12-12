from random import choice
series = [3,2,5,7,4,9,1,6,8,10,'a','c','l','d','e']

winning_ticket = []
print("Let's see what the winning ticket is...")

while len(winning_ticket) < 4:
    pulled_item  = choice(series)

    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")        