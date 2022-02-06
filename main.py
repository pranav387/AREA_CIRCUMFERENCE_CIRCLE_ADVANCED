import programSETTINGS as s
import os
import math
from termcolor import colored
from time import sleep
# getting path

if s.ALWAYS_SET_TO_DEFAULT_PATH == False:
    print("Please provide the path of which folder this file is in. Example path: C:\\Users\\prana\\Desktop\\vscode_venv_projects\\portfolio_programs\\area_of_circle")
    print("You can set ALWAYS_SET_DEFAULT_PATH to True to not ask this again.\n")
    path = input("\nWe need the path to make sure that this project works on your computer. Enter 'DEFAULT' for default path in settings: ")
    if path == "DEFAULT" or path == "default":
        os.chdir(s.DEFAULT_PATH)
    else:
        os.chdir(path)
elif s.ALWAYS_SET_TO_DEFAULT_PATH == True:
    os.chdir(s.DEFAULT_PATH)
    print("\nThe path has been automatically set to default path.")
else:
    print("ERROR OCCURRED: Invalid value provided for ALWAYS_SET_TO_DEFAULT setting.")

# printing current settings
# change settings in another file called programSETTINGS.py
settings = open("programSETTINGS.py", 'r')
print("\nCurrent settings:\n"+settings.read()+"\n")
# print(s.ROUND_OFF_VALUES)
settings.close()
    
if s.RUN_PROGRAM == False:
    print(colored("FATAL ERROR OCCURRED: Please set RUN_PROGRAM to True otherwise the program cannot run.", 'red'))
    sleep(5)
    exit()
elif s.RUN_PROGRAM == True:
    pi = math.pi
    #
    print("\nPlease type r before entering the number for radius, or d for diameter.\n")
    # Getting the user inputs necessary to calculate the area, and the circumference of the circle.
    num = input("Enter the radius or diameter of a circle: ")
    unit = input("Enter unit: ")
    # Checking whether the user entered radius or diameter for value.
    if num[0] == 'r':
        # radius input calculation
        num = num.replace('r','')
        num = float(num)
        d = num*num
        area = pi*d
        circum = 2*pi*num
        if s.ROUND_OFF_VALUES == True:
            area = round(area)
            circum = round(circum)
        if s.SHOW_ONLY_AREA == False:
            print(f"Area is {area}{unit}\u00b2. Circumference is {circum}{unit}.")
            sleep(5)
        if s.SHOW_ONLY_AREA == True:
            print(f"Area is {area}{unit}\u00b2.")
            sleep(5)
        exit()
    elif num[0] == 'd':
        # diameter input calculation
        num = num.replace('d','')
        num = float(num)
        rad = num/2
        area = pi*rad*rad
        circum = 2*pi*rad
        if s.ROUND_OFF_VALUES == True:
            area = round(area)
            circum = round(circum)
        if s.SHOW_ONLY_AREA == False:
            print(f"Area is {area}{unit}\u00b2. Circumference is {circum}{unit}.")
            sleep(5)
        if s.SHOW_ONLY_AREA == True:
            print(f"Area is {area}{unit}\u00b2.")
            sleep(5)
        exit()
    else:
        # Non functional user input data received
        print(colored("ERROR OCCURRED: Please follow the user input rules. Put r or d before entering the number.", 'red'))
        more_info = input("More info about user input in this program(y/n): ")
        if more_info == 'y':
            print(colored("""Please type r before entering the number for radius, or d for diameter. Rerun the program to try again.""", 'green'))
        elif more_info == 'n':
            print("Program is being exited.")
            sleep(2.5)
        else:
            pass
        exit()
else:
    print(colored("ERROR OCCURRED: Error occurred due to invalid RUN_PROGRAM setting.", 'red'))
    sleep(3.5)
    exit()
#TO DO: Make Graphical User Interface(GUI) version of this program.
