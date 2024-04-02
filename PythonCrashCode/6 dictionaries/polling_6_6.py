favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}
who_take_poll = ['jen','edward','Hieu','Kaneki']
for who in who_take_poll:
    who_alredy_poll = set(favorite_languages.keys())
    if(who in who_alredy_poll):
        print(f"Thanks {who.title()} for responding")
    else:
        print(f"{who.title()}! You should take the poll!")
