import requests
import json
from route import getRoute
route = getRoute()
def  getUserPosts(username = "", publicKey = "",  numToFetch = 10, mediaRequired = False, lastPostHash= "",readerPublicKey = "BC1YLianxEsskKYNyL959k6b6UPYtRXfZs4MF3GkbWofdoFQzZCkJRB"):
    payload = {"PublicKeyBase58Check":publicKey,
                "Username":username,
                "ReaderPublicKeyBase58Check":readerPublicKey,
                "LastPostHashHex":lastPostHash,
                "NumToFetch":numToFetch,
                "MediaRequired":mediaRequired}

    endpointURL = route + "get-posts-for-public-key"
    response = requests.post(endpointURL, json = payload)
    return response.json()

def getPostInfo(postHash, commentLimit = 20, fetchParents = False, commentOffset = 0, addGlobalFeedBool = False, readerPublicKey = "BC1YLianxEsskKYNyL959k6b6UPYtRXfZs4MF3GkbWofdoFQzZCkJRB",):
    payload = {"PostHashHex":"",
            "ReaderPublicKeyBase58Check":readerPublicKey,
            "FetchParents":fetchParents,
            "CommentOffset":commentOffset,
            "CommentLimit":commentLimit,
            "AddGlobalFeedBool":addGlobalFeedBool}

    endpointURL = route + "get-single-post"
    response = requests.post(endpointURL, json = payload)
    return response.json()
        
