class Match:
    def __init__(self):
        self.playerDict = {}

    def addPlayer(self, userID, position, accelerationRate, radius, mass):
        self.playerDict[userID] = Player(position, accelerationRate, radius, mass)

    def start(self):
        return

    def getPlayerLocation(self, userID):
        return self.playerDict[userID].getPosition()

    def setPlayerInput(self, userId, input):
        return
    
class Player:
    def __init__(self, position, accelerationRate, radius, mass):
        self.position = position
        self.speed = [0, 0]
        self.acceleration = [0, 0]
        self.accelerationRate = accelerationRate
        self.radius = radius
        self.mass = mass
    
    def getPosition(self):
        return self.position

    def getRadius(self):
        return self.radius

    def move(self):
        return

    def updateDirection(self, playerInput):
        return

    def checkCollision(self):
        return

    def bounce(self):
        return

    def isInBounds(self):
        return True

