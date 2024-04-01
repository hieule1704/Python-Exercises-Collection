from pathlib import Path

path = Path('guest_book.txt')
guest_book = []
guest_name = input("Enter guest name: \nEnter 'quit' to end the program.")
while guest_name!='quit':
    guest_book.append(guest_name)
    guest_name = input("Enter guest name: \nEnter 'quit' to end the program.")
guest = ''
for g in guest_book:
    guest=guest+g+"\n"
path.write_text(guest)