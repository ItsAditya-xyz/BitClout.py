import json
import requests
def getCloutPrice():
    response = requests.get("https://api.blockchain.com/v3/exchange/tickers/CLOUT-USD")
    return response.json()
    
