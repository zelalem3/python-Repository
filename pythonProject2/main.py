alphabet = ['a' , 'b', 'c' , 'd' 'e' , 'f', 'g' , 'h' ,'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))
def encrypt(plain_text,shift_amount):
     for letter in plain_text:
       shift_amount=shift_amount[i+shift_amount]
       print(shift_amount)

encrypt(text,shift)