cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)

cubes2 = []
for cube in range(1,11):
    cube = cube**3
    cubes2.append(cube)
for cube in cubes2:
    print(cube)