import os

print("-----Welcome to the Jungle-----")

status = True
while status == True:
    choose = input("Press 'L' to Login , Press 'S' to Signup (L/S): ")
    if choose == "S":
        saved_username = input("Enter your username you want to use : ")
        saved_password = input("Enter your password you want to use : ")
        password_verify = input("Repeat your password : ")
        if password_verify == saved_password:
            users_dict = dict()
            
            users_dict[saved_username] = saved_password
            users_list = open("users.txt", "a")
            print(type(str(users_dict)))
            users_list.write(str(users_dict)),
            users_list.close
        elif password_verify == saved_password:
            print("Passwords do not match.")
    elif choose == "L":
        usernamelogin = input("Please enter your username : ")
        passwordlogin = input("Please enter your password : ")
        if (usernamelogin == saved_username)  & (passwordlogin == saved_password):
            print("Succesfully Logined")
            print(users_dict)
        else:
            print("You entered your username or password incorrectly")
