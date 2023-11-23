import random
answer = random.randint(1,100)
print("welcome to the guessing game!!!")
level = input("enter the level you want(choose 'hard' or 'easy'")
guess=input("enter your guess")
def check_answer:
    if guess == answer:
        print("you got it right")
    elif guess