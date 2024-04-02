from pathlib import Path
import json

def get_new_favNum(path):
    user_num = input("Input your favorite number: ")
    content = json.dumps(user_num)
    path.write_text(content)
    return content
def get_stored_favNum(path):
    content = path.read_text()
    user_num = json.loads(content)
    return user_num

path = Path('favorite_number.json')
if path.exists():
    user_num = get_stored_favNum(path)
    print(f"Your favorite number is {user_num}")
else:
    user_num = get_new_favNum(path)