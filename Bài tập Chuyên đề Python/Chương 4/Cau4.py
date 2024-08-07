#Viết hàm tính ROI ( Return in investment )
def calculateROI(cost, revenue):
    roi = (revenue-cost)/cost
    return roi

def determineInvest(roi):
    if(roi>0.75):
        return True
    return False

#Main
cost = float(input("Nhập vào chi phí đầu tư: "))
revenue = float(input("Nhập vào loi nhuan: "))
if(determineInvest(calculateROI(cost, revenue))):
    print("Nên đầu tư!")
else:
    print("Không nên đầu tư!")