print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
from random import randint
HM
def difficulty():
    h = input("choose a difficulty. Type 'easy' or  'hard'\n")
    if h == "easy":
        print("You have 10 attempts remaining to guess the number.")
    elif h == "hard":
        print("You have 5 attempts remaining to guess the number.")
    else:
        print("you have inserted invalid input.")
difficulty()
def level(guess, answer):
    guess = int(input("Make a Guess: "))
    answer = randint(1, 100)
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print(f"you got it, The answer is {answer} ")

level(guess, answer)