from part_time_employee import *
from full_time_employee import *
from calculate_wages import *

def display_menu():
    print()
    print("1. Employee Login")
    print("2. Manager Login")
    print()
    print("Please select an option from the above menu")

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

def login():
    display_menu()
    choice = select_option()
    if choice == 1:
        pass
    if choice == 2:
        pass
    return login

def loginPage():
    print()
    print("1. Calculate Wages")
    print("2. Ammend Personal Information")
    print()
    print("Please select an option from the above menu")

def loginPageChoice():
    loginPage()
    choice = select_option()
    if choice == 1:
        employeeTypeChoice()
    if choice == 2:
        ammend_info()
    return loginPageChoice




if __name__ == "__main__":
    login()
    loginPageChoice()
    
