import requests
import json
import Route

class Posts:

    route = Route.getRoute()
    def  getUserPosts(self, username = "", publicKey = "",  numToFetch = 10, mediaRequired = False, lastPostHash= "",readerPublicKey = "BC1YLianxEsskKYNyL959k6b6UPYtRXfZs4MF3GkbWofdoFQzZCkJRB"):
        payload = {"PublicKeyBase58Check":publicKey,
                    "Username":username,
                    "ReaderPublicKeyBase58Check":readerPublicKey,
                    "LastPostHashHex":lastPostHash,
                    "NumToFetch":numToFetch,
                    "MediaRequired":mediaRequired}

        endpointURL = self.route + "get-posts-for-public-key"
        response = requests.post(endpointURL, json = payload)
        return response.json()

    def getPostInfo(self, postHash, commentLimit = 20, fetchParents = False, commentOffset = 0, addGlobalFeedBool = False, readerPublicKey = "BC1YLianxEsskKYNyL959k6b6UPYtRXfZs4MF3GkbWofdoFQzZCkJRB",):
        payload = {"PostHashHex":"",
                "ReaderPublicKeyBase58Check":readerPublicKey,
                "FetchParents":fetchParents,
                "CommentOffset":commentOffset,
                "CommentLimit":commentLimit,
                "AddGlobalFeedBool":addGlobalFeedBool}

        endpointURL = self.route + "get-single-post"
        response = requests.post(endpointURL, json = payload)
        return response.json()
            
