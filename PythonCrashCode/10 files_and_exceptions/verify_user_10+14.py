from pathlib import Path
import json

path = Path('user_dictionary.json')

def add_new_username(path,user_name):
    user_dict = {}
    user_dict['user_name'] = user_name
    user_dict['age'] = input("Enter your age: ")
    user_dict['height'] = input("Enter your height(cm): ")
    path.write_text(json.dumps(user_dict))

user_name = input("Enter your name: ")
content = json.loads(path.read_text())
if user_name == content['user_name']:
    print(f"Welcome back {user_name}")
else:
    add_new_username(path,user_name)
    content = json.loads(path.read_text())
    print(f"Welcome {content['user_name']}")
    