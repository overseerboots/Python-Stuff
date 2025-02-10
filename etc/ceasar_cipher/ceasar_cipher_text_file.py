filename = input("Enter file name\n> ")

def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("0. Exit")
    choice = int(input("Enter your choice\n> "))
    return choice

with open (filename, "r") as f:
    file_contents = f.read()

with open (filename, "w") as f:
    shift = 0

    choice = menu()

    if choice == 0:
        quit()

    elif choice == 1:
        encrypted_text = ""
        unencrypted_text = file_contents
        shift = int(input("Enter the shift\n> "))
        for letter in unencrypted_text:
            encrypted_text += chr(ord(letter) + shift)
        f.write(encrypted_text)
        print("File written :)")

    elif choice == 2:
        unencrypted_text = ""
        encrypted_text = input("Enter the text you want to decrypt\n> ")
        shift = int(input("Enter the shift\n> "))
        for letter in encrypted_text:
            unencrypted_text += chr(ord(letter) - shift)
        f.write(unencrypted_text)
        print("File written :)")

    else:
        input("Invalid choice.")