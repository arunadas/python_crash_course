def show_messages(messages):
    """Print all the messages"""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """send all the messages"""

    # send message to the new list
    # move each design to sent messages
    while messages:
        current_message = messages.pop()
        print(f"current message , {current_message}")
        sent_messages.append(current_message)


    # print sent meesage 
    for sent_message in sent_messages:
        print(f"{sent_message}")

messages = ['how are you', 'hello','hows the wheather']  
show_messages(messages)

sent_messages = []
# sent the copy of the list and keep original
send_messages(messages[:], sent_messages)

print("\nFinal lists: ")
print(messages)
print(sent_messages)
