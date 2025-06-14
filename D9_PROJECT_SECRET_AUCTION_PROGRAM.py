def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount == highest_bid:
            print("Draw")
            break
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\n🏆 The winner is {winner} with a bid of ₹{highest_bid}.")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name? : ")
    price = int(input("What is your Bid? : ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        print("\nList of all bidders and their bids:")
        for bidder, amount in bids.items():
            print(f"{bidder} : ₹{amount}")

        find_highest_bidder(bids)
        continue_bidding = False
    elif should_continue == "yes":
        print("\n" * 10)




