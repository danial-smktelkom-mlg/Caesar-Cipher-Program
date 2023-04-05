# Caesar-Cipher-Program

Caesar Cipher Encryption and Decryption Program

Introduction:

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet. This shift value is often referred to as the "key". In this program, we implement the Caesar cipher encryption and decryption techniques using Python.

Program Description:

The program consists of three functions: caesar_encryption(), caesar_decryption(), and caesar_cipher(). The caesar_encryption() function takes a plain text message and a shift value as input and returns the encrypted message. The caesar_decryption() function takes an encrypted message as input and returns all possible decrypted messages by iterating through all possible shift values. The caesar_cipher() function provides a menu for the user to either encrypt or decrypt a message using the Caesar cipher or exit the program.

The program begins by displaying a menu for the user to choose from. If the user chooses option 1, the caesar_encryption() function is called and the user is prompted to enter the plain text message and the shift value. The function then returns the encrypted message. If the user chooses option 2, the caesar_decryption() function is called and the user is prompted to enter the encrypted message. The function then returns all possible decrypted messages by iterating through all possible shift values. If the user chooses option 0, the program exits. If the user enters an invalid choice, the program prompts the user to try again.

Conclusion:

In conclusion, this program implements the Caesar cipher encryption and decryption techniques using Python. The program provides a menu for the user to either encrypt or decrypt a message using the Caesar cipher or exit the program. The Caesar cipher is a relatively simple encryption technique, but it can be useful in certain situations where security is not a major concern.
