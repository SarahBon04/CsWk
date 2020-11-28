from lib import music, login




def login_menu():
    login_user = ""
    print("1) Register?\n2) login? ")
    menu = int(input("Enter 1 or 2 "))
    if menu == 1:
        username = input("Input new username login ")
        print(login.register_user(username))
        login_user = ""
    elif menu == 2:
        username = input("Input username ")
        login_result = login.login_user(username)
        if login_result == "Successful login":
            login_user = username
        else:
            login_user = ""
            print("Username doesn't exist ")
    return login_user


        





if __name__ == "__main__":
    logged_in_user = ""
    while logged_in_user == "":
        logged_in_user = login_menu()
    print("Start game")

