from pathlib import Path

def read_file(path):
    """Read conttent from file's path"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn's exist!")
    else:
        print(contents)

while True:
    path = Path(str(input("Enter your file's path you want to read:")))
    read_file(path)
    message = input("Do you have any file left to read(Y/N): ")
    if message == 'N':
        break