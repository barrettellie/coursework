class EmployeeLogin():
    """Employee Login"""

    def __init__(self):
        super().__init__()

    def login(self, username, password):
        username = "barrettellie"
        password = "hello"
        username = input("Please enter your username: ")
        if username == True:
            password = input("Please enter your password: ")
            if password == True:
                print("Welcome. You have successfully logged in!")
            else:
                print("The password you entered was incorrect. Please try again.")
        else:
            print("The username you entered was incorrect. Please try again.")

        
if __name__ == "__main__":
    ALogin = EmployeeLogin()
    ALogin.login("username", "password")
