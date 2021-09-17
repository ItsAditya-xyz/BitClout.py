class Route:
    ROUTE = "https://bitclout.com/api/v0/"
    def getRoute(self):
        return self.ROUTE

    def setRoute(self, route):
        #you can route the APIs to other nodes ex. https://love4src.com/api/v0/ etc.
        self.ROUTE = route
