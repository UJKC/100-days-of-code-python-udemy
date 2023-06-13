print("Bidding System")

bidder ={}
def compute(bidder):
    max = 0
    winner = ""
    for anal in bidder:
        amount = bidder[anal]
        if amount > max:
            max = amount
            winner = anal
            print(f"{winner} is the winner")

biddingfinished = False

while not biddingfinished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bidder[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    compute(bidder)
  elif should_continue == "yes":
    print("continue")