#Tinh BMI

def calculateBMI(height,weight):
    bmi=weight/(height*height)
    return bmi

def giveSuggestionBaseBMI(bmi):
    type, risk = '', ''
    if(bmi<18.5):
        type = 'Under weight'
        risk = 'Low'
    elif bmi>=18.5 and bmi<25:
        type = 'Normal'
        risk = 'Medium'
    elif bmi>=25 and bmi<30:
        type = 'Over weight'
        risk = 'High'
    elif bmi>=30 and bmi<35:
        type = 'Obesity Class I'
        risk = 'High'
    elif bmi>=35 and bmi<40:
        type = 'Obesity Class II'
        risk = 'Very High'
    else:
        type = 'Obesity Class III'
        risk = 'Warming'
    print(f"Your bmi is {round(bmi,2)} - Type: {type} & Risk of epidemic disease: {risk}")

#Main
weight = float(input("Enter your weight in kilogram: "))
height = float(input("Enter your height in meters: "))
giveSuggestionBaseBMI(calculateBMI(height,weight))