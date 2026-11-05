from getpass import getpass

islogin = False

while islogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == "zai " and password == "edzillangz":
        print("Login successful!")
        islogin = True
    else:
        print("Invalid username or password. Please try again.")
        islogin = False