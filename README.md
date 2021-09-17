# BitClout.py

A python package for bitclout.

Developed by [ItsAditya](https://bitclout.com/u/itsaditya)

## Examples of How To Use BitClout.py

Getting $CLOUT price
```python
import bitclout
print(bitclout.Clout.getCloutPrice())
```

Getting user(s) info through publicKey(s)
```python
import bitclout
import json
with open("userInfo.json", "w") as file:
    listOfPublicKeys = ["BC1YLjJVhcVAi5UCYZ2aTNwRMtqvzQar4zbymr7fyinu8MsWLx2A1g1"] # you can pass multiple public key of users
    json.dump(bitclout.Users.getUserStateless(listOfPublicKeys))
```

Getting user info through BitClout username
```python
import bitclout
import json
with open("userInfo.json", "w") as file:
    username = "ItsAditya" 
    json.dump(bitclout.Users.getSingleProfile(username))

```

Getting users who are blocked by a profile
```python
import bitclout
import json
with open("blockedUsers.json", "w") as file:
    publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" # well, that's my (@ItsAditya) public key :)
    json.dump(bitclout.Users.getUsersBlocked(publicKey))
```

Getting user posts
```python
import bitclout
import json
with open("UserPosts.json", "w") as file:
    json.dump(bitclout.Posts.getUserPosts(username="ItsAditya"))
```
More docs coming soon!

Found any issue ? Report us on our repo: https://github.com/AdityaChaudhary0005/BitClout.py

Tip the author of this module some #CLOUT at: https://bitclout.com/u/ItsAditya (even 1 diamond counts :)