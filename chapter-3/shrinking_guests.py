guests = ['picaso', 'trovolta','therman']

print(f"{guests[0].title()} can\'t make to the dinner")
guests[0] = 'nicole'
guests.insert(0,'vivekananda')
guests.insert(3,'arbindo')
guests.append('subash')

print(f"Sorry can invite only two people")
guest_name = guests.pop()
print(f"Sorry {guest_name} have only 2 seats will invite later")
guest_name = guests.pop()
print(f"Sorry {guest_name} have only 2 seats will invite later")
guest_name = guests.pop()
print(f"Sorry {guest_name} have only 2 seats will invite later")
guest_name = guests.pop()
print(f"Sorry {guest_name} have only 2 seats will invite later")

print(f"{guests[0].title()} , you are invited to dinner this saturday!")
print(f"{guests[1].title()} , you are invited to dinner this saturday!")

del guests[0]
del guests[0]
