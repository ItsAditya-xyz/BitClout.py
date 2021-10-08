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

### Getting wallet of a user through public key

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

Found any issue ? Report us on our [repo](https://github.com/AdityaChaudhary0005/BitClout.py)

Tip the author of this module some #CLOUT at: [@ItsAditya](https://bitclout.com/u/ItsAditya) (even 1 diamond counts :)

### Buying creator coin of a user

```python
from bitclout import *

''' SEEDHEX should always be kept private. It has access to your complete wallet. It's kinda like
    seed phrase. This is why writing methods in backend isn't a good practice until we have derived keys.
    You can only automate your own account and can't have user authorisation. It is recommended to use test account while using write methods.

    You can find the seedHex of your account in your browser storage. Just open https://bitclout.com/ > Dev tools > Application > Storage > Local Storage > https://identity.bitclout.com > users > Select the public key with which you want to post > seedHex'''
SEEDHEX = "" # you seedHex
PUBLIC_KEY = "" #you PublicKey


PublicKeyToBuy = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" 
trade = Trade(SEEDHEX, PUBLIC_KEY)
status = trade.buy(keyToBuy = PublicKeyToBuy, DeSo = 0.1) # you are buying 0.1 DeSO of the creator's coin
print(status)  #200 if transaction was succesfull
```

### Selling creator coin of a user

```python
from bitclout import *

''' SEEDHEX should always be kept private. It has access to your complete wallet. It's kinda like
    seed phrase. This is why writing methods in backend isn't a good practice until we have derived keys.
    You can only automate your own account and can't have user authorisation. It is recommended to use test account while using write methods.

    You can find the seedHex of your account in your browser storage. Just open https://bitclout.com/ > Dev tools > Application > Storage > Local Storage > https://identity.bitclout.com > users > Select the public key with which you want to post > seedHex'''
SEEDHEX = "" # you seedHex
PUBLIC_KEY = "" #you PublicKey


publicKeyToSell = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" 
trade = Trade(SEEDHEX, PUBLIC_KEY)
status = trade.sell(keyToSell = publicKeyToSell, sellMax = True)# you are selling max coins of the creator
print(status)  #200 if transaction was succesfull
```

### Sending a post on bitclout

```python
from bitclout import Post

''' SEEDHEX should always be kept private. It has access to your complete wallet. It's kinda like
    seed phrase. This is why writing methods in backend isn't a good practice until we have derived keys.
    You can only automate your own account and can't have user authorisation. It is recommended to use test account while using write methods.

    You can find the seedHex of your account in your browser storage. Just open https://bitclout.com/ > Dev tools > Application > Storage > Local Storage > https://identity.bitclout.com > users > Select the public key with which you want to post > seedHex'''
SEEDHEX = ""  # your seedHex
PUBLIC_KEY = ""  # your PublicKey

post = Post(SEEDHEX, PUBLIC_KEY)

status = post.send("This post was sent using the bitclout python library 😎")
print(status)  # 200 if post was successfull
```

### Sending direct message on bitclout
```python
from bitclout import Message
import json

SEEDHEX = "" # your seed Hex
PUBLIC_KEY = "" #your public Key
msg = Message(SEEDHEX, PUBLIC_KEY)
text = "This is a direct message made using bitclout.py"
recipientKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
status = msg.send(recipientKey, text)
print(status)  # 200 if post was successfulld
```