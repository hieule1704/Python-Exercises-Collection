from pathlib import Path

path = Path('learning_python.txt') #Relative path

contents = path.read_text().replace('Python', 'Java')
print(contents)

print("\n")

for line in contents.splitlines():
    print(line)