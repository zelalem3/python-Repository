print("welcome to the bdding software")




def highest_bidder(highbid):
    for bid in highbid:
     bid_amount = highbid[bid]
     highest_bidder = 0
     if bid_amount > highest_bidder:
        highest_bidder=highbid
     bider=bid
    print("the highest biddes is {bidder} with the bid of {highest bidder}")
bidding_finished = False
while not bidding_finished:
    name = input("what is your name?")
    price = int(input("enter your bid?"))
    auction_dictionary = {}
    auction_dictionary[name] = price
    action = input("is there any other other bidder? say 'yes' or 'no' ")
    if action=="no":
        bidding_finished= True

highest_bidder(auction_dictionary)