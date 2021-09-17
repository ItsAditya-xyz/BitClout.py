import json
import requests

class Clout:
    def getCloutPrice(): #returns clout price
        response = requests.get("https://api.blockchain.com/v3/exchange/tickers/CLOUT-USD")
        return response.json()
    
