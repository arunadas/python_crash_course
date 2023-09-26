rivers = {'ganga':'india',
          'yamuna':'india',
          'saraswati':'india'
          }

for k , v in rivers.items():
    print(f"river {k.title()} runs through {v}")

print("\n")
print(f"Follwoing are all the rivers")
for key in rivers.keys():
    print("river :" , key)

for country in set(rivers.values()):
    print(f"country: ", country)

print(int('11',2))    
