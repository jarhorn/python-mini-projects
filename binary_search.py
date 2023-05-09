print("Welcome to binary search!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
print()

def binary_search(search_list, element):
    middle=0
    start=0
    end=len(search_list)
    steps=0
    search_list = list(map(int, search_list))
    element = int(element)

    while(start<=end):
        print("Step", steps, ":", str(search_list[start:end+1]))
        steps += 1
        middle = (start + end) // 2

        if element == search_list[middle] :
            return middle
        elif element < search_list[middle] :
            end = middle - 1
        else:
            start = middle + 1

    return -1

print("Here is an example of the binary search")
print()
my_list = [2,3,5,7,11,13,17,19,23,29]
my_target = 17
print("Starting list: ", my_list)
print("Target: ", my_target)
binary_search(my_list, my_target)

print()
print("Now let's try some numbers you provide")
your_list = input("Please provide a list of numbers to search separated by pipe ('|') character: ").split("|")
your_target = input("Please provide the number will you target from the list: ")
binary_search(your_list, your_target)
