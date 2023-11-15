def send_messages(messages):
    """send all the messages"""
    
    sent_messages = []

    # send message to the new list
    # move each design to sent messages

    while messages:
        current_message = messages.pop()
        print(f"current message , {current_message}")
        sent_messages.append(current_message)


    # print sent meesage 
    for sent_message in sent_messages:
        print(f"{sent_message}")

    print(f"original message list,{messages}")
    print(f"sent message ,{sent_messages}")    

messages = ['how are you', 'hello','hows the wheather']  
send_messages(messages[:])