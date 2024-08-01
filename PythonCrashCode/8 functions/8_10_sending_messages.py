#Cách 1 import module_name
# import message_module
#
# messages = ["Have a good day!", "Be present", "Focus on work"]
# sent_messages = []
# message_module.sending_messages(messages, sent_messages)
# print("List messages sent: ")
# message_module.show_messages(sent_messages)
# print("List messages not sent: ")
# message_module.show_messages(messages)

#Cách 2 from module_name import function_name
# from message_module import sending_messages, show_messages
#
# messages = ["Have a good day!", "Be present", "Focus on work"]
# sent_messages = []
# sending_messages(messages, sent_messages)
# print("List messages sent: ")
# show_messages(sent_messages)
# print("List messages not sent: ")
# show_messages(messages)

#Cách 3 from module_name import function name as fn
# from message_module import sending_messages as sd, show_messages as sm
#
# messages = ["Have a good day!", "Be present", "Focus on work"]
# sent_messages = []
# sd(messages, sent_messages)
# print("List messages sent: ")
# sm(sent_messages)
# print("List messages not sent: ")
# sm(messages)

#Cách 4 import module_name as mn
# import message_module as mm
#
# messages = ["Have a good day!", "Be present", "Focus on work"]
# sent_messages = []
# mm.sending_messages(messages, sent_messages)
# print("List messages sent: ")
# mm.show_messages(sent_messages)
# print("List messages not sent: ")
# mm.show_messages(messages)

#Cách 5 from module_name import *
from message_module import *

messages = ["Have a good day!", "Be present", "Focus on work"]
sent_messages = []
sending_messages(messages, sent_messages)
print("List messages sent: ")
show_messages(sent_messages)
print("List messages not sent: ")
show_messages(messages)