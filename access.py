import sys

name = input("Name: ")

if name == "Jackson":
    pin = input("PIN: ")

    if pin == "7464":
        password = input("Password: ")

        if password == "rocket186":
            print("Access Granted")
            access = True
        else:
            print("Access Denied")
            access = False
    else:
        print("Access Denied")
        access = False

else:
    print("Access Denied")
    access = False

if access is True:
    print("My bank account number is 12345")

elif access is False:
    print("The authorities have been called")
