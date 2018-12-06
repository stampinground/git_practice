"""
Calculate BMI. BMI = weight / height^2 where weight is in kg and height meters.

underweight BMI < 18.5
normal BMI >= 18.5 but < 25.0
overweight >= 25.0 but < 30.0
obese >= 30.0
"""

print ("This is a BMI calculator")
print ("")

height = float(input("What is your height (meters)?: "))
weight = float(input("What is your weight (kg)?: "))
BMI = weight / (height**2)

print ("")
print ("Your BMI is %s" % (BMI))

def bmi_range(BMI):
    if BMI <= 18.5:
        print("You are underweight.")
    elif BMI >= 18.5 and BMI < 25:
        print("You have a normal BMI.")
    elif BMI >= 25 and BMI < 30:
        print("You are overweight.")
    else:
        print("You are obese!")

def normal(weight):
    normal_when = (height**2) * 25
    difference = int(weight - normal_when)
    print("You would need to weigh %skg less to have a normal BMI" % (difference))

def obese(height):
    obese_when = (height**2) * 30
    print("You would need to weigh %skg to be obese" % (int(obese_when)))

bmi_range(BMI)
normal(weight)
obese(height)
