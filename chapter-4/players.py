players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
# -ve to get items from end , 3rd onwards
print(players[-3:])
# third item to skip
print(players[::2])

print("Here are the first three players of my team")
for player in players[:3]:
    print(player.title())