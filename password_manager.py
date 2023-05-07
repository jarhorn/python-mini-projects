from cryptography.fernet import Fernet

'''
# writes key file (only run ONCE!)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:",user, "| Password:", fer.decrypt(passw.encode()))

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


master_password = input("What is the master password? ")
key = load_key()
fer = Fernet(key)

while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view/quit) ").lower()
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "quit" or mode == "q":
        break
    else:
        print("Invalid mode.")
        continue