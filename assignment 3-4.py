side1 = float(input("enter the leight of side1:"))
side2 = float(input("enter the leight of side2:"))
side3 = float(input("enter the leight of side3:"))

if (side1 == side2 == side3):
    print("equilateral triangel")
elif (side1==side2 or side2==side3 or side1==side3):
    print("isoceles")
else:
    print("scalene")
