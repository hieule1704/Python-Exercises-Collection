people_num = {
    'Hieu':[4,17,8],
    'Anh':'3',
    'Hưng':[3,2],
    'Mẫn':'9',
    'Khang':'4',
}
for key,value in people_num.items():
    #print(f"{key} favorite number is {value}")
    if(len(value)==1):
        print(f"{key} favorite number is {value}")
    else:
        print(f"{key} favorite number is: ")
        for v in value:
            print(v)
