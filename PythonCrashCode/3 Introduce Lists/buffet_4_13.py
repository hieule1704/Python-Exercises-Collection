foods = ("Bánh xèo","Cơm chiên","Phở","Hủ tiếu","Tôm rang me")
print("Old menu: ")
for food in foods:
    print(food)
# foods[0] = "Bún bò" # TypeError: 'tuple' object does not support item assignment
foods = ("Bún bò","Sinh tố","Phở","Hủ tiếu","Tôm rang me")
print("New menu: ")
for food in foods:
    print(food)

