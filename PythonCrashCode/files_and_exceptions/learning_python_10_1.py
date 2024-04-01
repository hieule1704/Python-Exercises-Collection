from pathlib import Path

path = Path('learning_python.txt') #Relative path
contents = path.read_text().replace("Python","Java")
print(contents)

#lines = contents.splitlines()
for line in contents.splitlines():
    print(line)