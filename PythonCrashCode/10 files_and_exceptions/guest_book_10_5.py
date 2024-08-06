from pathlib import Path

path = Path('guest_book.txt')
guest_book = []

while True:
    guest_name = input("Enter 'quit' to end the program!\nEnter guest name: ")
    if guest_name=='quit':
        break
    guest_book.append(guest_name)

guest = ''
for g in guest_book:
    guest=guest+g+"\n"
path.write_text(guest)