alphabet = ['a' , 'b', 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' ,'q', 'r', 's','t','u','v','w','x','y','z']

direction=input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("type your message:\n")
shift=int(input("type the shift number:\n"))

def encrypt(plain_text,shift_amount):
  for letter in plain_text:
    cipher_text=" "
    position = alphabet.index(letter)
    new_position= position + shift_amount
    new_letter=alphabet(new_position)
    cipher_text  +=new_letter
    print(f"the encoded text is {cipher_text}")
encrypt(plain_text,shift_amount,alphabet)
def decrypt(plain_text,shift_amount):
    for letter in plain_text:

        position=alphabet.index(plain_text)
        new_position=position - shift_amount
        new_letter=alphabet(new_position)
        print("the encoded text is {new_Letter}")