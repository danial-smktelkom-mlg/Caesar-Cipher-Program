text = input("Insert encrypted text : ")

a = 26
b = 0
encryption = ""

while b < a:
    print("Decrypted text by", b, "is : ")

    for i in text:
        if i.isupper():
            i_unicode = ord(i)
            i_index = ord(i) - ord("A")
            new_index = (i_index - b) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encryption = encryption + new_character

        elif i.islower():
            i_indexLower = ord(i) - ord("a")
            new_indexLower = (i_indexLower - b) % 26
            new_unicodeLower = new_indexLower + ord("a")
            new_character2 = chr(new_unicodeLower)
            encryption = encryption + new_character2

        else:
            new_indexspace = ord(" ")
            new_character3 = chr(new_indexspace)
            encryption = encryption + new_character3

    print(encryption)

    encryption = ""
    b += 1
