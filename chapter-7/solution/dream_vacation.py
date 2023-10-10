prompt = "If you could visit one place in the world, "
prompt += "where would you go? "


responses = {}

while True:
    name = input("What is your name? ")
    place = input(prompt)
    responses[name] = place

    repeat = input("Do you want someone else to poll? yes/no ")

    if repeat == 'no':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} wants to visit {place.title()}")
  