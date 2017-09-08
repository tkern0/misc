# Gets an float from the user
# Can handle text inputs
def getPrice(prompt):
    while True:
        try:
            result = float(input(prompt))
            if result < 0: raise ValueError
        except ValueError:
            print("Please enter a positive number")
        else:
            break
    return round(result, 2)

reserve = getPrice("What is the reserve price")
bids = {}
hBid = 0

print("Auction has started")
while True:
    print("Highest bid so far is ${:.2f}".format(hBid))
    name = input("What is your name?")
    if name:
        bid = getPrice("What is your bid?")
        if bid < hBid:
            print("Sorry {}, you'll need to make another, higher bid.".format(name))
        else:
            bids[name] = bid
            hBid = bid
    else:
        while True:
            finished = input("Are you sure you want to finish? [Y/N]")
            if finished.lower() in ("y", "n", "yes", "no"):
                break
            else:
                print("Please enter \"Y\" or \"N\"")
        if finished in ("y", "yes"): break

bidderOrder = []
priceOrder = sorted(bids.values())
for price in priceOrder:
    for bidder in bids:
        if bids[bidder] == price:
            bidderOrder.append(bidder)
            break

if hBid > reserve: print("\nAction won by {} with a bid of ${:.2f}".format(bidderOrder[-1], hBid))
else: print("\nAuction did not meet reserve price")
for bidder, price in zip(bidderOrder, priceOrder):
    print("{} bid ${:.2f}".format(bidder, price))
