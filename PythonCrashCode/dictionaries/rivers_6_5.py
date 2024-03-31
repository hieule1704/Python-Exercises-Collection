rivers = {
    'nile':'egypt',
    'amazon':'brazil',
    'truong giang':'china'
}
for key,value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}!")
print("Name of each river: ")
for river_name in rivers.keys():
    print(river_name.title())
print("Name of each country: ")
for country in rivers.values():
    print(country.title())