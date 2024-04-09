import lottery

my_ticket = "1704"
win_ticket = ""
n=1
while my_ticket != win_ticket:
    win_ticket = str(lottery.lottery())
    print(f"{n} - {win_ticket}")
    n+=1