#!/bin/usr/python3

# With the aid of a function and a dictionary, write an interactive python programme that will ask the user the following questions

# 1. What's your name ?
# 2. How old are you ?
# 3. What is your favourite colour ?
# 4. Do you like Python ?
# The world is flat: True or False ?

# Then based on their answers, make some comments back to them

def ask_qs():
    data = {}

    while True:
        name = input("What is your name? ")
        if name and not name.isdigit():
            data["Name"] = name
            break
        print("Innvalid input, please try again only entering acceptable characters and letters.")

    while True:
        try:
            age = int(input("How old are you? "))
            if age >- 0:
                data["Age"] = age
                break
            print("Age cannot be negative, please try again.")
        except ValueError:
            print("Invalid input, please enter your age as an integer.")

    while True:
        fav_color = input("What is your favourite color? ")
        if fav_color and not fav_color.isdigit():
            data["Fav_color"] = fav_color
            break
        print("Invalid input, please try again")

    while True:
        like_python = input("Do you like Python? (y/n) ")
        if like_python in ["yes", "y", "no", "n"]:
            if like_python == "yes" or "y":
                data["Likes_python"] = "Yes"
            else:
                data["Likes_python"] = "No"
            break
        print("Invalid input, please try again with either (y/n).")

    while True:
        world_flat = input("The world is flat: True or False? ").lower()
        if world_flat in ["true", "t", "false", "f"]:
            if world_flat == "true" or "t":
                data["World_flat"] = "True"
            else:
                data["World_flat"] = "False"
            break
        print("Invalid input, please enter only either 'True' or 'False'.")

    return data


def comment_user(data):
    name = data["Name"]
    like_python = data["Likes_python"]

    print("Hello", name)

    if like_python == "Yes":
        print("I'm glad you like python!")
    else:
        print("Is there something we can do to make you like python more?")


def main():
    print("Interrogating the user...")

    user_data = ask_qs()
    comments = comment_user(user_data)

if __name__ == "__main__":
    main()
