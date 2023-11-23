print("welcome to the top calculator.")
bill=input("what was the total bill? $")
people=input("how many people to split the bill? ")
tip=input("what percentage tip would you like to give? 10,12,14 or 15?")
totalbill=float(bill) / float(people)
percentage_tip_int=float(totalbill)*float(tip)/100
the_total=totalbill + percentage_tip_int
the_total_amount=round(the_total,2)
print(f"each person should pay {the_total_amount} dollar")
