import random

# Functions =====================================
def options_entry():
    options = []
    error = 1
    while error == 1:
        try:
            options.append(int(input("Password length\n> ")))
            error = 0
        except:
            print("Error: Invalid input, please enter a positive integer")
    error = 1
    while error == 1:
        try:
            choice = (input("Special characters? [Y/n]\n> "))
            if choice == "Y" or choice == "y" or choice == "":
                options.append(True)
            elif choice == "N" or choice == "n":
                options.append(False)
            error = 0
        except:
            print("Error: Invalid input")
    error = 1
    while error == 1:
        try:
            options.append(int(input("Amount of passwords to print\n> ")))
            error = 0
        except:
            print("Error: Invalid input, please enter a positive integer")
    return options

def save_options(options):
    with open("password_generator_options.txt", "w") as f:
        for line in range(0,3):
            line = ""
        f.write("length: "+str(options[0])+"\n")
        f.write("special_characters: "+str(options[1])+"\n")
        f.write("password_count: "+str(options[2])+"\n")

def use_saved_options():
    with open("password_generator_options.txt", "r") as f:
        options = f.read()
        options = options.split()
        options.remove("length:")
        options.remove("special_characters:")
        options.remove("password_count:")
        options[0] = int(options[0])
        options[2] = int(options[2])
    return options

# End of functions ==============================


# The program ===================================

## Options ======================================
ask_use_saved_options = input("Use saved options? [Y/n]\n> ")
if ask_use_saved_options == "n" or ask_use_saved_options == "N":
    print("Setting new options...")
    options = options_entry()
    ask_save_options = input("Save options? (Will overwrite existing options) [Y/n]\n> ")
    if ask_save_options == "Y" or ask_save_options == "y" or ask_save_options == "":
        save_options(options)
else:
    options = use_saved_options()

## Generation ===================================
print("====================")

for password_num in range(0,options[2]): # Password count
    passwords = []
    output = ""
    if options[1] == "True": # Has special characters
        for password_char in range(0,options[0]): # Password length
            output += chr(random.randint(33,126))
        passwords.append(output)
    else: # No special characters
        for password_char in range(0,options[0]): # Password length
            while True:
                rand_num = random.randint(65,122)
                if (rand_num < 91 and rand_num > 64) or (rand_num < 123 and rand_num > 96):
                    output += chr(rand_num)
                    break
        passwords.append(output)
    print(output)
print("====================")