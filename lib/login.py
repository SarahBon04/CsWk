import pickle
import os.path

#Registering a new user
def register_user(username):
    user_list = load_list()
    if username in user_list:
        result = "User exists"
    else:
        user_list.append(username)
        with open("user_list.data", "wb") as myfile:
            pickle.dump(user_list, myfile)
        result = "Register successful"
    return result 

def login_user(username):
    user_list = load_list()
    if username in user_list:
        result = "Successful login"
    else:
        result = "Username not found"
    return result



def load_list():
    user_list = []
    if os.path.exists("user_list.data"):
        with open("user_list.data", "rb") as myfile:
            user_list = pickle.load(myfile)
    return user_list




if __name__ == "__main__":
    #print(register("Sarah"))
    #print(register("Becky"))
    print(load_list())
    print(register_user("Jess"))
    print(load_list())