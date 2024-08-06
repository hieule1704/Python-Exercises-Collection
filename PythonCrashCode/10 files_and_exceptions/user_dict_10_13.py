from pathlib import Path
import json

path = Path('user_dictionary.json')

user_dict = {}
while True:
    user_dict['user_name'] = input("Enter your name: ")
    user_dict['age'] = input("Enter your age: ")
    user_dict['height'] = input("Enter your height(cm): ")
    path.write_text(json.dumps(user_dict))
    break
print(type(json.loads(path.read_text())))
print(type(path.read_text()))