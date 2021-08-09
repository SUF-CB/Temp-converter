# Python Math & Time Modules
import math
import time

# Intro
print("Welcome to the Temperature Conventer. Type C for Celsuis, F for Fahreinheit ")

def Loop():
    # Letting the user choose the temperature and convert it to another temperature else
    userchoicetemperature =input("Please choose your current unit of temperature (C (degrees), F (Farenheight)>>")
    converttemperature =input("Now choose the unit of temperature you want to conver to  (C (degrees), F (Farenheight)>>")

    if userchoicetemperature == "C":
        if converttemperature == "F":
            degree = float(input("enter the degree: "))
            result = (degree * 9/5) + 32
            print(f"{result}°F ")
        elif converttemperature == "C":
            print("This is the same type of temperature")
            again()
        else:
            print("Type a temperature")
            again()

    elif userchoicetemperature == "F":
        if converttemperature == "C":
            degree = float(input("enter the Farenheight: "))
            result = (degree - 32) * 5/9
            print(f"{result}°C")
        elif convert_Temperature == "F":
            print("This is the same type of temperature")
            again()
        else:
            print("Type a temperature")
            
Loop()
