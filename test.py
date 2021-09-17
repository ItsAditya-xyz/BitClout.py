import bitclout
import json
with open("diamondsReceived.json", "w") as file:
    publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
    diamondData = bitclout.Diamonds.getDiamonds(publicKey=publicKey, received=True)
    '''reveived is an optional arguement when true it returns diamond received by users else
    return diamonds give by users'''
    json.dump(diamondData, file)