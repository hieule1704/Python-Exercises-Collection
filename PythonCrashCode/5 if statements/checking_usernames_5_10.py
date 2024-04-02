current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['user5', 'user6', 'user7', 'USER2', 'user1']

current_users_copy = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f'Sorry {new_user}, that name is already taken.')
    else:
        print(f'Welcome {new_user}! Your user name is available.')

