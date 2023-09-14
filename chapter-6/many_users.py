users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'elinstein',
        'location' : 'princeton'
    },

    'mucurie':{
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    },
}

for username , user_info in users.items():
    print(f"\n Username : {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\t Location: {location.title()}")    