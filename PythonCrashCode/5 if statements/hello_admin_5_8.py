usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
#usernames = []
if usernames == []:
    print('We need to find some users!')
else:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')