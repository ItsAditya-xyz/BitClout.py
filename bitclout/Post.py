import requests
from bitclout.Route import getRoute
from bitclout.Sign import Sign_Transaction


class Post:
    def __init__(self, seedHex, publicKey):
        self.SEED_HEX = seedHex
        self.PUBLIC_KEY = publicKey

    def send(self, content, imageUrl=[]):
        header = {
            "content-type": "application/json"
        }

        payload = {"UpdaterPublicKeyBase58Check": self.PUBLIC_KEY,
                   "PostHashHexToModify": "",
                   "ParentStakeID": "",
                   "Title": "",
                   "BodyObj": {"Body": content, "ImageURLs": imageUrl},
                   "RecloutedPostHashHex": "",
                   "PostExtraData": {},
                   "Sub": "",
                   "IsHidden":  False,
                   "MinFeeRateNanosPerKB": 1000
                   }
        ROUTE = getRoute()
        endpointURL = ROUTE + "submit-post"
        res = requests.post(endpointURL, json=payload, headers=header)
        transactionHex = res.json()["TransactionHex"]

        signedTransactionHex = Sign_Transaction(
            self.SEED_HEX, transactionHex
        )  # txn signature

        submitPayload = {"TransactionHex": signedTransactionHex}
        endpointURL = ROUTE + "submit-transaction"
        submitResponse = requests.post(endpointURL, json=submitPayload)
        return submitResponse.status_code  # returns 200 if buy is succesful
