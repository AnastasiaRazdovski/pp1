height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
height = height / 100
bmi = weight / (height ** 2)
print(bmi)
if bmi < 25: print(" Correct weight: True" )
else: print(" Correct weight: False" )