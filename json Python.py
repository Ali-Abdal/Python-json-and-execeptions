import json

file = "idk.json"

def check_user(username):
    print("awnser with yes/no: ")

    awnser = input(f"\nare you {username}? ")

    if awnser == "yes":
        print(f"greetings {username}")

    else:
        set_new_username()

def set_new_username():

    username = input("what is your name? ")

    with open(file,"w") as f:
        json.dump(username,f)

def get_username():

    try:
        with open(file,"r") as f:
            content = json.load(f)

    except Exception:
        return None

    else:
        return content

def greet_user():

    username = get_username()

    if username:
        check_user(username)

    else:
        set_new_username()
        
greet_user()