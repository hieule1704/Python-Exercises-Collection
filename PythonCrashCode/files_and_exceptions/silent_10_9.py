from pathlib import Path

def read_file(path):
    """Read conttent from file's path"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contents)

while True:
    path = Path(str(input("Enter your file's path you want to read:")))
    read_file(path)
    message = input("Do you have any file left to read(Y/N): ")
    if message == 'N':
        break