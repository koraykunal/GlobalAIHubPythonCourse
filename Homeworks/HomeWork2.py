print("-----Welcome to the Jungle-----")

username = "Koray"
password = "11515qaswed"

usernamelogin = input("Please enter your username : ")
passwordlogin = input("Please enter your password : ")

if (usernamelogin == username)  & (passwordlogin == password):
    print("Succesfully Logined")
elif (usernamelogin != username)  & (passwordlogin == password):
    print("You entered your username incorrectly")
elif (usernamelogin == username)  & (passwordlogin != password):
    print("You entered your password incorrectly")
else:
    print("You entered your username and password incorrectly")