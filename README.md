# BitClout.py

A python package for bitclout.

Developed by [ItsAditya](https://bitclout.com/u/itsaditya)

## Examples of How To Use BitClout.py

Getting $CLOUT price
```python
from bitclout import *
print(getCloutPrice())
```

Getting user(s) info through publicKey(s)
```python
from bitclout import *
import json
with open("userInfo.json", "w") as file:
    listOfPublicKeys = ["BC1YLjJVhcVAi5UCYZ2aTNwRMtqvzQar4zbymr7fyinu8MsWLx2A1g1"] # you can pass multiple public key of users
    json.dump(getUserStateless(listOfPublicKeys))
```

Getting user info through BitClout username
```python
from bitclout import *
import json
with open("userInfo.json", "w") as file:
    username = "ItsAditya" 
    json.dump(getSingleProfile(username))

```

Getting users who are blocked by a profile
```python
from bitclout import *
import json
with open("blockedUsers.json", "w") as file:
    publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg" # well, that's my (@ItsAditya) public key :)
    json.dump(getUsersBlocked(publicKey))
```


More docs coming soon!