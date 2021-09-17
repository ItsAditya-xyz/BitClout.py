import bitclout
publicKey = "BC1YLhBLE1834FBJbQ9JU23JbPanNYMkUsdpJZrFVqNGsCe7YadYiUg"
#priniting the public key of users who are blocked by the above public key
print(bitclout.Users.getUsersBlocked(publicKey))

#getting basic user info
print(bitclout.Users.getSingleProfile(username="ItsAditya"))

#getting posts made by a user
print(bitclout.Posts.getUserPosts(username="ItsAditya"))