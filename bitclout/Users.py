import requests
import json
import Route

class Users:
    route = Route.getRoute()

    def getUserStateless(self, publicKeyList, skipForLeaderboard = True):
        '''when skipForLeaderboard is true, it doesn't return info like UsersYouHODL,
            followers public key and blocked users'''
        payload = {"PublicKeysBase58Check": publicKeyList,"SkipForLeaderboard":skipForLeaderboard}
        endpointURL = self.route + "get-users-stateless"
        response = requests.post(endpointURL, json = payload)
        return response.json()

    def getSingleProfile(self, publicKey= "", username = "",):
        payload = {"PublicKeyBase58Check": publicKey, "Username": username}
        endpointURL = self.route + "get-single-profile"
        response = requests.post(endpointURL, json = payload)
        return response.json()

    def getProfilePic(publicKey):
        profilePicURL = f'https://bitclout.com/api/v0/get-single-profile-picture/{publicKey}?fallback=https://bitclout.com/assets/img/default_profile_pic.png'
        return profilePicURL

    def getUsersBlocked(self, publicKey):
        payload = {"PublicKeysBase58Check": [publicKey],"SkipForLeaderboard":False}
        endpointURL = self.route + "get-users-stateless"
        response = requests.post(endpointURL, json = payload)
        return response.json()["UserList"][0]["BlockedPubKeys"]

    def getWallet(self, publicKey, includeCreatorCoin = True): 
        #returns $CLOUTs in wallet and Creators coins on whom the user has invested in
        try:
            payload = {"PublicKeysBase58Check": [publicKey],"SkipForLeaderboard":False}
            endpointURL = self.route + "get-users-stateless"
            response = requests.post(endpointURL, json = payload)
            responseJson = response.json()
            print(response.json())
            finalResponse = {
            }
            if includeCreatorCoin:    
                coinHeld = responseJson["UserList"][0]["UsersYouHODL"]
                finalResponse["CoinsHeldInfo"] = coinHeld

            CloutInWallet = responseJson["UserList"][0]["BalanceNanos"]
            print(CloutInWallet)
            finalResponse["CloutInWalletNanos"] =  CloutInWallet
            return finalResponse
        except Exception as e:
            return response.status_code

    def getHodlers(self, username =  "", publicKey= "", lastPublicKey= "", numToFetch = 100, fetchAll = False):
        payload = {"PublicKeyBase58Check":publicKey,
                    "Username":username,
                    "LastPublicKeyBase58Check":lastPublicKey,
                    "NumToFetch":numToFetch,
                    "FetchHodlings":False,
                    "FetchAll":fetchAll}
        
        endpointURL = self.route + "get-hodlers-for-public-key"
        response = requests.post(endpointURL, json = payload)
        return response.json()





