print("Welcome to choose your own adventure!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")

name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end.  You can go left or right.  Which way would you like to go? ").lower()
if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across.  Type 'walk' to walk around or 'swim' to swim across. ").lower()
    if answer == "swim":
        print("While swimming, you were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died thirsty.")
    else:
        print("Not a valid option. You lose!")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly.  Do you want to attempt to cross or head back? Type 'cross' to give it a go or 'back' to head back. ").lower()
    if answer == "back":
        print("You go back to the main road.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger.  Do you talk to them? (yes/no) ").lower()
        if answer == "yes":
            print("Being a good samaritan pays off, they give you gold and you WIN!")
        else:
            print("As you walk by the stranger, you are stabbed in the back by them.  You die from your injury.")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")