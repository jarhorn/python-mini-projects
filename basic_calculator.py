print("Welcome to basic calculator!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
print()

def add_ints(addends):
    sum=0
    for addend in addends:
        print("Adding ", addend, " to ", sum)
        sum += int(addend)

    return sum

def subtract_ints(minuend, subtrahends):
    subtrahends_total = add_ints(subtrahends)
    print("Subtracting ", subtrahends_total, " from ", minuend)
    return (int(minuend) - subtrahends_total)

def multiply_ints(factors):
    product=int(factors.pop(0))
    for factor in factors:
        print("Multiplying ", factor, " by ", product)
        product *= int(factor)

    return product

def divide_ints(dividend, divisors):
    divisor_total = multiply_ints(divisors)
    print("Dividing ", dividend, " by ", divisor_total)
    return (int(dividend) / divisor_total)

while True:
    print()
    print("Addition (A)")
    print("Subtraction (S)")
    print("Multiplication (M)")
    print("Division (D)")
    print("Quit (Q)")
    print()
    choice = input("Please choose mathematical function (A, S, M, D, or Q): ").lower()
    print()

    if len(choice) > 0:
        choice = choice[0]
        if choice == "a":
            print("You chose addition.")
            addends = input("Please supply a list of addends to add separated by the pipe ('|') character: ").split("|")
            print("The sum is: ", add_ints(addends))
        elif choice == "s":
            print("You chose subtraction")
            minuend = input("Please provide the minuend for the equation: ")
            subtrahends = input("Please supply a list of subtrahends to subtract from the minuend separated by the pipe ('|') character: ").split("|")
            print("The difference is: ", subtract_ints(minuend, subtrahends))
        elif choice == "m":
            print("You chose multiplication.")
            factors = input("Please supply a list of factors to multiply separated by the pipe ('|') character: ").split("|")
            print("The product is: ", multiply_ints(factors))
        elif choice == "d":
            print("You chose division")
            dividend = input("Please provide the dividend for the equation: ")
            divisors = input("Please supply a list of divisors to divide from the dividend separated by the pipe ('|') character: ").split("|")
            print("The quotient is: ", divide_ints(dividend, divisors))
        elif choice == "q":
            print("Thanks for playing!")
            quit()
        else:
            print("The option provided '", choice, "' is not valid, please try again")
            print()
            continue
    else:
        print("Your option must contain at least one character, please try again.")
        print()
        continue


        
            



