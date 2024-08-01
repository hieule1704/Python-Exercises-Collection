def show_messages(messages):
    for message in messages:
        print(message)

def sending_messages(messages, sent_messages):
    while messages:
        curent_message = messages.pop(0)
        print(curent_message)
        sent_messages.append(curent_message)