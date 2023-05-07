import random

print("Welcome to rock/paper/scissors game!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    # check input
    if user_input not in options:
        continue

    # rock = 0, paper = 1, scissors = 2
    user_pick_index = options.index(user_input)
    computer_pick_index = random.randint(0,2)
    
    computer_pick = options[computer_pick_index]
    print(f"Computer picked: {computer_pick}, user picked: {user_input}")

    if user_pick_index == computer_pick_index:
        print("It's a draw... no winner!")
    elif (user_pick_index + 1) % 3 == (computer_pick_index % 3):
        print("Computer wins!")
        computer_wins += 1
    else:
        print("User wins!")
        user_wins += 1
    
print()
print("Okay, we're done playing... here's the results:")
print(f"You won {user_wins} times... Computer won {computer_wins} times.")
print("Goodbye!")