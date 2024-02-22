from morse import values
import sys


def encrypt():
    text = input("Enter the word you want to encrypt: ")
    morse_code = ""
    text = text.upper()

    for i in text:

        for key, value in values.items():
            if i == key:

                morse_code += str(value)
                morse_code += " "

    print(morse_code)


def decrypt():
    encrypted = input("Enter the morse code you want to be deciphered ")
    text = " "
    encrypted = encrypted.split()

    for i in encrypted:

        for key, value in values.items():
            if i == value:
                text += str(key)
                text += " "
    if len(text) == 0:
        print("you didn't enter a valid code")
    else:
        print(text)


choice = input("Welcome! Do you want to encrypt or decrypt press 1 to encrypt and 2 to decrypt? ")


if choice == "1":
    encrypt()
elif choice == "2":
    decrypt()
else:
    sys.exit("you did not input the right number!!!please try again")
