height = input("Enter Your Height in Meters :   ")
weight = input("Enter Your Weight in Kg =  ")

height_c = float(height)
weight_c = float(weight)

bmi = weight_c / (height_c**2)
print("Your BMI is : ", int(bmi))
