import random
word_list = ["ardvark", "babbon", "camel"]
choosen_word = random.choice(word_list)
print(choosen_word)
guess = input("guess the letter").lower()
for letter in choosen_word:
    if letter == guess :
        print("correct")
    else:
        print("incorrect")
display=[]
for position in choosen_word:
    display+="_"
print(display)
for position in range(len(choosen_word)):
    letter=choosen_word[position]
    if guess==letter:
        display[position] = letter
        print(display)





