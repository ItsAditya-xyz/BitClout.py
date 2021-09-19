# BitClout.py

A python package for bitclout.

Developed by [ItsAditya](https://bitclout.com/u/itsaditya)

Run `pip install bitclout` to install the module!
## Examples of How To Use BitClout.py

### Getting $CLOUT price
```python
import bitclout
print(bitclout.Clout.getCloutPrice())
```

### Getting user(s) info through publicKey(s)
```python
import bitclout
import json
with open("userInfo.json", "w") as file:
    listOfPublicKeys = ["BC1YLjJVhcVAi5UCYZ2aTNwRMtqvzQar4zbymr7fyinu8MsWLx2A1g1"] # you can pass multiple public key of users
    json.dump(bitclout.Users.getUserStateless(listOfPublicKeys), file)
```

### Getting user info through BitClout username
```python
import bitclout
import json
with open("userInfo.json", "w") as file:
    username = "ItsAditya" 
    json.dump(bitclout.Users.getSingleProfile(username=username), file) #you can also pass publicKey = "<public key of any user>" here instead of username just in case you want to get the profile info from public key
```

### Getting profile pic through public key
```python
import bitclout
publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" # well, that's my (@ItsAditya) public key :)
print(bitclout.Users.getProfilePic(publicKey))
```
Getting wallet of a user through public key 
```python
import bitclout
import json
publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" 
with open("wallet.json", "w") as file:
    walletData = bitclout.Users.getWallet(publicKey, includeCreatorCoin = True) # make includeCreatorCoin as false when you don't want to have creator coin investment in the response data
    json.dump(walletData, file)
```

### getting creator coin holders of a user
```python
import bitclout 
import json
publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
with open("investors.json", "w") as file:
    investorData = bitclout.Users.getHodlers( username =  "", publicKey= publicKey, lastPublicKey= "", numToFetch = 100, fetchAll = False)
    # well, you can play around with above list of args to get what you want :)
    json.dump(investorData, file) 
```
### Getting users who are blocked by a profile
```python
import bitclout
import json
with open("blockedUsers.json", "w") as file:
    publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" # well, that's my (@ItsAditya) public key :)
    json.dump(bitclout.Users.getUsersBlocked(publicKey), file)
```

### Getting user posts
```python
import bitclout
import json
with open("UserPosts.json", "w") as file:
    json.dump(bitclout.Posts.getUserPosts(username="ItsAditya"), file)
```
### Getting information about single post ( likes, comments etc on a post)
```python
import bitclout
import json
with open("UserPosts.json", "w") as file:
    postHash = "52f9b2dc7f616a94d583a5a167bb49ba7558279e06bdd0642b1777246a6570a2" #the hash of the post. you can find this in post URL :)

    postInfo = bitclout.Posts.getPostInfo(postHash, commentLimit = 20, fetchParents = False, commentOffset = 0, addGlobalFeedBool = False, readerPublicKey = "BC1YLianxEsskKYNyL959k6b6UPYtRXfZs4MF3GkbWofdoFQzZCkJRB")

    json.dump(postInfo, file)
```

#### Getting diamond information about a user (received or sent)
```python
import bitclout
import json
with open("diamondsReceived.json", "w") as file:
    publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
    diamondData = bitclout.Diamonds.getDiamonds(publicKey=publicKey, received=True)
    '''reveived is an optional arguement when true it returns diamond received by users else
    return diamonds give by users'''
    json.dump(diamondData, file)
```

### Getting deleted posts of a user
```python
import bitclout
import json

#public Key of @DiamondHands
publicKey = "BC1YLgU67opDhT9bTPsqvue9QmyJLDHRZrSj77cF3P4yYDndmad9Wmx" 
with open("HiddenPosts.json", "w") as file:
    json.dump(bitclout.Posts.getHiddenPosts(publicKey), file)
```
More docs coming soon!

Found any issue ? Report us on our repo: https://github.com/AdityaChaudhary0005/BitClout.py

Tip the author of this module some #CLOUT at: https://bitclout.com/u/ItsAditya (even 1 diamond counts :)
