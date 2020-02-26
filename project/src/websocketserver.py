import asyncio
import json
import websockets
import threading
import concurrent.futures
import match

class GameServer:
    def __init__(self):
        self.PORT = 8081

        self.testMatch = match.Match()
        self.matchThread = threading.Thread(target=self.testMatch.runGameLoop, daemon=True)
        self.isMatchStarted = False
        print("Creating new game server.")

    async def on_message(self, ws, path):
        userID = ""
        while(True):
            message = await ws.recv()
            message = json.loads(message)

            if (message["type"] == "newConnection"):
                userID = message["id"]
                if (self.isMatchStarted == False):
                    self.testMatch.addPlayer(userID, [400, 500], 0.25, 30, 1)
                    print("New connection at websocket " + str(ws) + " with id " + userID)
                    outMsg = json.dumps({
                        "type": "info",
                        "body": "Joined match."
                    })
                    await ws.send(outMsg)
                else:
                    outMsg = json.dumps({
                        "type": "info",
                        "body": "Match already started, cannot join."
                    })
                    await ws.send(outMsg)
                    return
            if (message["type"] == "startMatch" and self.isMatchStarted == False):
                self.isMatchStarted = True
                print("Started match.")
                self.matchThread.start()
            if (message["type"] == "gameInput"):
                playerInputs = message["body"]
                inputX = playerInputs["right"] - playerInputs["left"]
                inputY = playerInputs["down"] - playerInputs["up"]
                self.testMatch.setPlayerInput(userID, inputX, inputY)

            # Send player data to client
            outData = {
                "type": "gameState",
                "matchState": self.testMatch.getMatchData(),
                "body": self.testMatch.getPlayerData()
            }
            if (outData["matchState"]["winner"] == userID):
                outData["matchState"]["youWin"] = True
            await ws.send(json.dumps(outData))
            
            if (outData["matchState"]["state"] == "finished"):
                break

    def start_game_server(self):
        print("Starting server at port " + str(self.PORT))
        start_server = websockets.serve(self.on_message, "localhost", self.PORT)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

testGameServer = GameServer()
testGameServer.start_game_server()
