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

    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print(f"Computer picked: {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie... No winner here!")
    else:
        print("You lost!")
        computer_wins += 1
    
print()
print("Okay, we're done playing... here's the results:")
print(f"You won {user_wins} times... Computer won {computer_wins} times.")
print("Goodbye!")