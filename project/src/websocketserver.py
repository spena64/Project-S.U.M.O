import asyncio
import json
import websockets
import threading
from online_user import OnlineUser
from game_queue import GameQueue

class GameServer:
    def __init__(self):
        self.PORT = 8081
        self.user_dict = {}
        self.lobby_dict = {}

        self.queue_duo = GameQueue()

    async def on_message(self, ws, path):
        user_id = ""

        while(True):
            message = await ws.recv()
            message = json.loads(message)

            if (message["type"] == "newConnection"):
                user_id = message["id"]

                # TODO: Authentiacate user

                print("New connection at websocket " + str(ws) + " with id " + user_id)
                self.user_dict[user_id] = OnlineUser(user_id)
                out_msg = {
                    "type": "info",
                    "body": "Connected to game server."
                }
                await ws.send(json.dumps(out_msg))
            if (message["type"] == "enqueue"):
                if (self.user_dict[user_id].status == "idle"):
                    if (message["body"] == "duo"):
                        self.queue_duo.add_user(user_id)
                        self.user_dict[user_id].status = "queueing"
                else:
                    out_msg = {
                        "type": "info",
                        "body": "Cannot queue for game, already in a queue or game."
                    }
                    await ws.send(json.dumps(out_msg))
            if (message["type"] == "gameInput"):
                # TODO: Find what lobby the player is in
                player_inputs = message["body"]
                input_x = player_inputs["right"] - player_inputs["left"]
                input_y = player_inputs["down"] - player_inputs["up"]
                # TODO: send inputs to lobby

            if (self.user_dict[user_id].status == "in lobby"):
                # TODO: get game state
                out_data = {
                    "type": "gameState",
                    "matchState": "",
                    "body": ""
                }
                #if (out_data["matchState"]["winner"] == user_id):
                    #out_data["matchState"]["youWin"] = True
                await ws.send(json.dumps(out_data))
            
        del self.user_dict[user_id]

    def start_game_server(self):
        print("Starting server at port " + str(self.PORT))
        start_server = websockets.serve(self.on_message, "localhost", self.PORT)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

test_game_server = GameServer()
test_game_server.start_game_server()
