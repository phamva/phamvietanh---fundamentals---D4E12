H = int(input("height"))
W = int(input("weight"))
CM = H/100
BMI = W/CM**2
print("BMI")
if BMI < 16:
    print("Severely underweight")
elif BMI >= 16 and BMI <=18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 25:
    print("Normal")
elif BMI >= 25 and BMI <= 30:
    print("Overweight")
else :
    print("sdfsd")

