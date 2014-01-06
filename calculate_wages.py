from full_time_employee import *
from part_time_employee import *

def calculate_wages():
    print()
    print("1. Full Time Employee")
    print("2. Part Time Employee")
    print()
    print("Please select your employee status from the above menu")

def select_option():
    choice = ""
    valid_option = False
    while not valid_option:
        try:
            choice = int(input("Option Selected: "))
            if choice in (1,2):
                valid_option = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def employeeTypeChoice():
    calculate_wages()
    choice = select_option()
    if choice == 1:
        full_time_main()
    if choice == 2:
        part_time_main()
    return employeeTypeChoice

if __name__ == "__main__":
    employeeTypeChoice()
