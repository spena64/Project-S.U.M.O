import time
import math

RING_CENTER_X = 500
RING_CENTER_Y = 500
RING_RADIUS = 450

class Match:
    def __init__(self):
        self.playerDict = {}
        self.state = "waiting"
        self.winner = "Undecided"

    def addPlayer(self, userID, position, accelerationRate, radius, mass):
        self.playerDict[userID] = Player(position, accelerationRate, radius, mass)

    def runGameLoop(self):
        # Game loop
        self.state = "started"
        while(True):
            inRingNum = 0
            for id in self.playerDict:
                player = self.playerDict[id]
                player.move()
                if (player.isInBounds()):
                    inRingNum += 1
            
            if (inRingNum == 1):
                break
            time.sleep(0.01)
        self.endMatch()

    def endMatch(self):
        self.state = "finished"
        for id in self.playerDict:
            player = self.playerDict[id]
            if (player.isInBounds()):
                self.winner = id

    def getMatchData(self):
        matchData = {
            "state": self.state,
            "winner": self.winner,
            "youWin": False
        }
        return matchData

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
        self.isAlive = True
    
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

        # Kill movement if out of bounds
        self.isAlive = math.sqrt( (self.position[0] - RING_CENTER_X) ** 2 + (self.position[1] - RING_CENTER_Y) ** 2 ) < RING_RADIUS
        if (self.isAlive == False):
            self.direction = [0, 0]
        return

    def setDirection(self, directionVector):
        if (self.isAlive == True):
            self.direction = directionVector
        return

    def checkCollision(self):
        return

    def bounce(self):
        return

    def isInBounds(self):
        return self.isAlive

