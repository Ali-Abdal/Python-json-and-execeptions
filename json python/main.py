import json

file = "idk.json"

def check_user(username):

    # checks if it's the same user or the old user 

    print("awnser with yes/no: ")

    awnser = input(f"\nare you {username}? ")

    if awnser == "yes":
        print(f"greetings {username}")

    else:
        set_new_username()

def set_new_username():

    # writes the new usernam to the json file

    username = input("what is your name? ")

    with open(file,"w") as f:
        json.dump(username,f)

def get_username():

    # gets the username from the json file and store it in a variable

    try:
        with open(file,"r") as f:
            content = json.load(f)

    except Exception:
        return None

    else:
        return content

def greet_user():

    #  if the username != null calls the function thats check if the user is the same user or new user
    #  if the username null call the function that asks the user for his name 

    username = get_username()

    if username:
        check_user(username)

    else:
        set_new_username()
        
greet_user()