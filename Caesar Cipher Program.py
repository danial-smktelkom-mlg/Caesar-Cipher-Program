def caesar_encryption():
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    symbolic = "~!@#$%^&*()-=+_`}{[]|':;><,./?"
    integer = "1234567890"
    
    shift = int(input("Enter shift value 0-25: "))
    text = input("Enter plain text: ")
    encrypted_text = ""
    
    for s in text:
        if s.isupper():
            s_index = alpha_upper.find(s)
            new_index = (s_index + shift) % 26
            new_char = alpha_upper[new_index]
            encrypted_text += new_char
        elif s.islower():
            s_index = alpha_lower.find(s)
            new_index = (s_index + shift) % 26
            new_char = alpha_lower[new_index]
            encrypted_text += new_char
        elif s == " ":
            encrypted_text += " "
        elif s.isnumeric():
            encrypted_text += s
        else:
            s_index = symbolic.find(s)
            new_char = symbolic[s_index]
            encrypted_text += new_char

    print("Encryption result:", encrypted_text)

def caesar_decryption():
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_lower = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    symbolic = "~!@#$%^&*()-=+_`}{[]|':;><,./?"
    integer = "1234567890"
    
    text = input("Enter plain text: ")
    
    for shift in range(26):
        decrypted_text = ""
        for s in text:
            if s.isupper():
                s_index = alpha_upper.find(s)
                new_index = (s_index - shift) % 26
                new_char = alpha_upper[new_index]
                decrypted_text += new_char
            elif s.islower():
                s_index = alpha_lower.find(s)
                new_index = (s_index - shift) % 26
                new_char = alpha_lower[new_index]
                decrypted_text += new_char
            elif s == " ":
                decrypted_text += " "
            elif s.isnumeric():
                decrypted_text += s
            else:
                s_index = symbolic.find(s)
                new_char = symbolic[s_index]
                decrypted_text += new_char

        print("Decryption result with shift", shift, ":", decrypted_text)

def caesar_cipher():
    print("Menu")
    print("0. Exit")
    print("1. Encryption")
    print("2. Decryption")
    option = input("Enter your choice: ")

    if option == "1":
        caesar_encryption()
    elif option == "2":
        caesar_decryption()
    elif option == "0":
        return
    else:
        print("Invalid choice, please try again.")
        caesar_cipher()

    caesar_cipher()

caesar_cipher()
