import random
def prime_checker(number):
    random_number=random.randint(1,10)
    if number == 1:
        print("it is neither prime nor composite")
    elif number%2!=0 and number%3!=0 and number%4!=0 and number%5!=0:
        print("it is prime")
    else:
        print("it is composite")







n = int(input("check this number: "))
prime_checker(number=n)