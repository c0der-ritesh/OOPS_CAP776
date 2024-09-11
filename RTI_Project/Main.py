from UserRegistration import User
from Login import UserLogin
from Dashboard import DashBoard

design = "-"*15

def ispassinfile(password,email):
    try:
        temp = email + ".txt"
        with open(temp, 'r') as userdata:
            for line in userdata:
                if f"{password}" in line:
                    return True
        return False
    except FileNotFoundError:
        return False


def isuserinfile(email):
    try:
        with open('Userdata.txt', 'r') as userdata:
            for line in userdata:
                if f"{email}" in line:
                    return True
        return False
    except FileNotFoundError:
        return False


def Query():
    print(f"Under construction !!")


def Dashboard(Dash):
    Dash.Userlog()
    Dash.start()
    while(1):
        print(f"\n 1. Raise your Query \n 2. Log out")
        n = int(input("Enter your choice : "))
        if n==1:
            Query()
        elif n==2:
            print("Logging out.....")
            break
        else:
            print("please enter valid option !!")
            

def Login():
    name = input("Enter your Email : ")
    password = input("Enter your Password : ")
    if isuserinfile(name) and ispassinfile(password,name):
        ULogin = DashBoard()
        ULogin.set_username(name)
        ULogin.set_password(password)
        print("Login Successful !!\n")
        Dashboard(ULogin)
    else:
        print("User not Exist, Please Register First !!")

    
def Register():
    name = input("Enter your Name : ")
    Email = input("Enter your email : ")
    password = input("Enter your password : ")
    confirmpassword = input("Re-enter your Password : ")
    if isuserinfile(Email):
        print(f"\n User Already registered !!")   
    else:
        if password == confirmpassword:
            NewUser = User()
            NewUser.set_Name(name)
            NewUser.set_Username(Email)
            NewUser.set_password(password)
            NewUser.save_Userdata()
            print(f"\n User Registered Successfully !! \n")
        else:
            print(f"\n Password and Re-enter Password Not match Try Again !! \n")
        

def firstscreen():
    while(1):
        print(f"\n {design} Welcome to RTI Portal {design}\n \n 1. Login to the Portal \n 2. New here? Register To the Portal \n 3. Exit the Portal \n")
        n = int(input("Enter your response : "))
        if n==1:
            Login()
        elif n==2:
            Register()
        else:
            print(f" {design} Bye {design} ")
            break


firstscreen()