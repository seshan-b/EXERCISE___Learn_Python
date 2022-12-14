# pylint: disable=import-error
import os
from graphic import logo
os.system('clear')





print(logo)

# Start with empty bid
bids = {}

# Track bid
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        
        
while not bidding_finished:
    # Get inputs
    name = input("What is your name?")

    price = input("What is your bid?")
    
    bids[name] = float(price)
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
       # Clearing the Screen
        os.system('clear')