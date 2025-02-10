def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("0. Exit")
    choice = int(input("Enter your choice\n> "))
    return choice

unencrypted_text = ""
encrypted_text = ""
shift = 0

choice = menu()

if choice == 0:
    quit()

elif choice == 1:
    unencrypted_text = input("Enter the text you want to encrypt\n> ")
    shift = int(input("Enter the shift\n> "))
    for letter in unencrypted_text:
        encrypted_text += chr(ord(letter) + shift)
    print("Encrypted text:\n"+encrypted_text)

elif choice == 2:
    encrypted_text = input("Enter the text you want to decrypt\n> ")
    shift = int(input("Enter the shift\n> "))
    for letter in encrypted_text:
        unencrypted_text += chr(ord(letter) - shift)
    print("Unencrypted text:\n"+unencrypted_text)
