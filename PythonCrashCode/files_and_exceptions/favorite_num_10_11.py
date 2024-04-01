from pathlib import Path
import json

fav_num = input("Enter your favorite number: ")

path = Path('favorite_number.json')
path.write_text(json.dumps(fav_num))

print(f"I know you favorite number! It's is {json.loads(path.read_text())}")