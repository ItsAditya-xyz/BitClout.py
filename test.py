import bitclout
with open("diamondsReceived.json", "w") as file:
    publicKey = "BC1YLg5JHBpXZS96bsYCCXBJfhwX4aBTZWjwLJmV6AHFWcA4pJvzPJh"
    diamondData = bitclout.Diamonds.getDiamonds(publicKey=publicKey, received=True)

    print("Total Diamonds received", len(diamondData["DiamondSenderSummaryResponses"]))