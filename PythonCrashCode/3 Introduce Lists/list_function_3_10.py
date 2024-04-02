list_ex = ["Yen Ngoc","Thi Dieu","Trang Anh","Nhu Y","Thi Ven","Ngoc Loan"]
print("Number of Hieu's ex: ",len(list_ex),"\nHere is them: ",list_ex)
list_ex.append("Ngan")
print("Xem la nguoi yeu: ",list_ex.pop())
list_ex.insert(0,"Thu Cuc")
print(list_ex[0],"tinh don phuong nam mau giao!")
del list_ex[0] #Xoa Thu Cuc vi don phuong deo tinh la ex
list_ex.remove("Thi Ven")
print(list_ex)
print(sorted(list_ex))
print(list_ex)
list_ex.reverse()
print(list_ex)
list_ex.sort()
print(list_ex)
#list_empty = []
#print(list_empty[-1])
