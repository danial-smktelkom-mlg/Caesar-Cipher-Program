shift = int(input("Insert shift key: "))
if shift < 1 or shift > 25:
    print("Shift key should be between 1 and 25.")
    exit()
text = input("Insert text : ")

encryption = []

for i in text:
    if i.isupper():
        i_unicode = ord(i)
        i_index = ord(i) - ord("A")
        new_index = (i_index + shift) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encryption.append(new_character)
        
    elif i.islower():
        i_indexLower = ord(i) - ord("a")
        new_indexLower = (i_indexLower + shift) % 26
        new_unicodeLower = new_indexLower + ord("a")
        new_character2 = chr(new_unicodeLower)
        encryption.append(new_character2)

    else :
        new_indexspace = ord(" ")
        new_character3 = chr(new_indexspace)
        encryption.append(new_character3)
        
encryption = "".join(encryption)

print("The plain text is : ", text)
print("The encrypted text is : ", encryption)
