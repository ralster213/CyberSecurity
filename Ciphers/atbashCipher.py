#Atbash Cipher
#Cipher must alter plaintext into its opposite letter in the alphabet
# N is the middle most character in the alphabet, and its opposite is N
# N is the 14th letter in the alphabet
# Will accept only letters in the alphabet
import sys
import pyperclip


run = 1
# to encrypt, plaintext will be converted to ciphertext by comparing the index of each plaintext character to its corresponding
# character from SYMBOLS, and swapped with the index of the corresponding CIPHER character
while run == 1:
    SYMBOLS = "abcdefghijklmnopqrstuvwxyz"
    CIPHER =  "zyxwvutsrqponmlkjihgfedcba"
    mode = input("Would you like to encrypt or decrypt a message? ")
    plaintext = input("Enter your message: ")
    plaintext = plaintext.lower()
    message = ""
    for symbol in plaintext:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)


            if mode == "encrypt":
                message += CIPHER[symbolIndex]
    
            elif mode == "decrypt":
                message += SYMBOL[symbolIndex]
            else:
                sys.exit("You Stupid!")
    pyperclip.copy(message)         
    print("Your new message is " + message)
    answer = input("would you like to run the program again? (yes/no)")
    if answer == "yes":
        pass
    elif answer == "no":
        run = 0
    else:
        print("bruh you really stupid. k i guess i'll shut it off dummy")
        run = 0

    