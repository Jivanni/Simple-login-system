#defining errors
class Error(Exception):
    pass
class Useralreadyexists(Error):
    pass
class Invalidcredentials(Error):
    pass

#opens the database with user information
with open("pass.txt","r") as filehandler:
    users = [user.split() for user in filehandler.readlines()]

# checks if username or email are already in database
def user_already_exists(email, username):
    flag = False
    for user in users:
        if email in user[0]:
            flag = True
    for name in users:
        if name in users[1]:
            flag = True
    return flag

#writes a new entry into the database after checking if the entry is already there
def registration(email,username,password):
    if user_already_exists(email, username):
        return False
    else:
        with open("pass.txt","a") as filehandler:
            filehandler.write("\n"+email+"\t"+username+"\t"+password)
        return True

#handles checks if the email and password combination entered by the user match any entries of the database
def login(email,password):
    flag = False
    for user in users:
        if email in user and password in user:
            flag = True
            login.username = user[1]
        
    return flag

#asks for user input and raises exceptions if an error occurs
def main():
    main.query = input("Please type 'register' if you would like to register a new account or 'login' to log-in: ")    
    if main.query == "register":
        email = input("Please enter an email address: ")
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        validity = registration(email,username,password)
        if validity is False:
            raise Useralreadyexists
        
    elif main.query == "login":
        email = input("Please enter your email address: ")
        password = input("Please enter your password: ")
        validity = login(email,password)
        if validity is False:
            raise Invalidcredentials
            
    return validity

if __name__ == '__main__':
    try:
        main()
        if main.query == "login":
            print(f"Success! Welcome: {login.username}")
        if main.query == "register":
            print("Account successfully created")
    except UnboundLocalError:
        print("Please enter a valid input")
    except Useralreadyexists:
        print("User already exists")
    except Invalidcredentials:
        print("Invalid credentials")