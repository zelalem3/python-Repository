print("welcome to the love calculator")
name1 = input("what is your name? \n")
name2 = input("what is their name? \n")
count = 0
combined_name = name1 + name2
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t + r + u + e
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
love = l + o + v + e
combiner = str(true) + str(love)
print(combiner)