# TODO-1: Ask the user for input
more_to_enter = "yes"
bid_dictionary = {}
while more_to_enter == "yes":
    name = input("What is your name?:")
    price = input("What is your bid?: $")
    bid_dictionary[name]=price
    more_to_enter = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    print("\n" * 20)

highest_bid = 0
highest_bidder=""
for key in bid_dictionary:
    if int(bid_dictionary[key]) > highest_bid:
        highest_bid=int(bid_dictionary[key])
        highest_bidder = key

print(f"Highest bid placed by {highest_bidder} for ${highest_bid}")


