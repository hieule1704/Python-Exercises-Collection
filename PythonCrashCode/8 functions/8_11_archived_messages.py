def show_messages(messages):
    for message in messages:
        print(message)

def sending_messages(messages, sent_messages):
    while messages:
        curent_message = messages.pop(0)
        print(curent_message)
        sent_messages.append(curent_message)

messages = ["Have a good day!", "Be present", "Focus on work"]
sent_messages = []
sending_messages(messages[:], sent_messages)
print("List messages sent: ")
show_messages(sent_messages)
print("List messages not sent: ")
show_messages(messages)
