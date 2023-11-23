import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10, 10]
users_rand = int (random.choice(cards))
secondusers_rand = int (random.choice(cards))

computer_rand = int (random.choice(cards))

secondcomputer_rand = int (random.choice(cards))
users_total = users_rand + secondusers_rand
print(f"{secondusers_rand} and {users_rand}")

print(f"the first computer random is {computer_rand}")
computer_total = computer_rand + secondcomputer_rand
if users_rand == 11 and users_total > 21:
    users_rand = 1
elif secondusers_rand == 11 and users_total > 21:
    secondusers_rand = 2
if computer_rand==11 and computer_total > 21 :
    computer_rand = 1
elif secondusers_rand == 11 and computer_total > 21:
    secondusers_rand=1
add_random_user = input("do you want to be hit with another number: enter 'Y' for yes and 'N' for no").lower()
if add_random_user== "n":
    print(f"your total is {users_total} and the computer total is {computer_total}")
    if computer_total > users_total:
          print("you lose")
    elif computer_total == users_total:
          print("draw")
    else:
          print("you win")


