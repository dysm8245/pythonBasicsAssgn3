from math import pi as p

def circumference():
    try:
        diameter = float(input("What is the diameter of the circle? Enter the number with units of feet.\n"))
        circ = diameter*p
        print(f"The circumference of a circle with a diameter of {diameter} feet is {circ} feet\n")
    except:
        print("You must enter a number value\n")

def houseArea():
    try:
        length = float(input("What is the length of your house? Enter the number with units of feet.\n"))
        width = float(input("What is the width of your house? Enter the number with units of feet.\n"))
        area = length*width
        print(f"The square footage of your house is {area} square feet\n")
    except:
        print("You must enter a number value\n")