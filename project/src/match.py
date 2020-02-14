import time

class Match:
    def __init__(self):
        self.playerDict = {}

    def addPlayer(self, userID, position, accelerationRate, radius, mass):
        self.playerDict[userID] = Player(position, accelerationRate, radius, mass)

    def runGameLoop(self):
        # Game loop
        while(True):
            for id in self.playerDict:
                player = self.playerDict[id]
                player.move()
        return

    def getPlayerLocation(self, userID):
        return self.playerDict[userID].getPosition()

    def setPlayerInput(self, userId, inputX, inputY):
        self.playerDict[userId].setDirection(inputX, inputY)
        return
    
class Player:
    def __init__(self, position, accelerationRate, radius, mass):
        self.position = position
        self.speed = [0, 0]
        self.direction = [0, 0]
        self.accelerationRate = accelerationRate
        self.radius = radius
        self.mass = mass
    
    def getPosition(self):
        return self.position

    def getRadius(self):
        return self.radius

    def move(self):
        self.speed[0] += self.direction[0] * self.accelerationRate
        self.speed[1] += self.direction[1] * self.accelerationRate

        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
        return

    def setDirection(self, inputX, inputY):
        self.direction[0] = inputX
        self.direction[1] = inputY
        return

    def checkCollision(self):
        return

    def bounce(self):
        return

    def isInBounds(self):
        return True

