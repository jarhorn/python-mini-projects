import random

print("Welcome to number guessing game!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

# get the upper bound for the random number
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print("Please type a number next time.")
    quit()

# generate a random number
print(f"Generating a random number between 0 and {top_of_range}")
random_number = random.randint(0, top_of_range)

# have the user try to guess the number
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    # check against random number
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Wrong, you were above the number... try again")
    else:
        print("Wrong, you were below the number... try again")

print(f"You guessed correctly in {guesses} tries.")