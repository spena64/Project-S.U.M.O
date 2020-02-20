import time
import math

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
            time.sleep(0.01)
        return

    def getPlayerState(self, userID):
        playerState = {
            "x": self.playerDict[userID].getPosition()[0],
            "y": self.playerDict[userID].getPosition()[1],
            "radius": self.playerDict[userID].getRadius()
        }
        return playerState

    def getPlayerData(self):
        playerData = {}
        for id in self.playerDict:
            playerData[id] = self.getPlayerState(id)
        return playerData

    def setPlayerInput(self, userId, inputX, inputY):
        directionVector = self.normalizeInput(inputX, inputY)
        self.playerDict[userId].setDirection(directionVector)
        print(directionVector)
        return

    def normalizeInput(self, x, y):
        magnitude = math.sqrt(x ** 2 + y ** 2)
        if (magnitude == 0):
            return [0, 0]
        
        return [x / magnitude, y / magnitude]
    
class Player:
    def __init__(self, position, accelerationRate, radius, mass):
        self.position = position
        self.speed = [0, 0]
        self.direction = [0, 0]
        self.accelerationRate = accelerationRate
        self.radius = radius
        self.mass = mass
        self.drag = 1.01
    
    def getPosition(self):
        return self.position

    def getRadius(self):
        return self.radius

    def move(self):
        self.speed[0] += self.direction[0] * self.accelerationRate
        self.speed[1] += self.direction[1] * self.accelerationRate

        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        self.speed[0] /= self.drag
        self.speed[1] /= self.drag

        # Stopping speed
        if (abs(self.speed[0]) < 0.1):
            self.speed[0] = 0
        if (abs(self.speed[1]) < 0.1):
            self.speed[1] = 0

        return

    def setDirection(self, directionVector):
        self.direction = directionVector
        return

    def checkCollision(self):
        return

    def bounce(self):
        return

    def isInBounds(self):
        return True

