import time

def find_and_replace_string(text, search_string, replace_string):
    print("Initial text: '", text, "'")
    updated_string = text.replace(search_string, replace_string)
    print("Updated text: '", updated_string, "'")
    return updated_string

print("Welcome to find and replace string!")
playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
print()

print("First, let's show off an example...")
print()
start_string = "The fast brown fox jumps over the lazy dog."
find_string = "fast"
replace_string = "quick"
print("Start string: '", start_string, "'\nFind string: '", find_string, "'\nReplace string: '", replace_string, "'")
print()
find_and_replace_string(start_string, find_string, replace_string)
print()

time.sleep(3)
print("Now, let's try something you create!")
print()
start_string = input("Enter your starting string of text: ")
find_string = input("Enter the string of text you'd like to replace: ")
replace_string = input("Enter the string of text you'd like to have in its place: ")
print("Start string: '", start_string, "'\nFind string: '", find_string, "'\nReplace string: '", replace_string, "'")
print()
find_and_replace_string(start_string, find_string, replace_string)
print()