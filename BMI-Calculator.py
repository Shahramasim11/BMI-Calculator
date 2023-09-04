print("Welcome to the BMI Calculator")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height in meters: "))
BMI = (weight / height**2)
print("Your BMI is:", BMI)
if BMI < 18.5:
    print("You are underweight: ")
elif BMI <= 25:
    print("You have normal weight: ")
elif BMI <= 30:
    print("You are overweight: ")
else:
    print("You are obese: ")