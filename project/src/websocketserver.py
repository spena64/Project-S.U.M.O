import asyncio
import json
import websockets
import threading
from online_user import OnlineUser
from game_queue import GameQueue
from lobby import DuoLobby

class GameServer:
    def __init__(self):
        self.PORT = 8081
        self.user_dict = {}
        self.lobby_dict = {}

        self.queue_duo = GameQueue(2)

        mm_thread_duo = threading.Thread(target=self.start_matchmaking_duo, daemon=True)
        mm_thread_duo.start()

    async def on_message(self, ws, path):
        user_id = "unknown"

        while(True):
            # Process incoming messages
            message = await ws.recv()
            message = json.loads(message)

            if (message["type"] == "newConnection"):

                # TODO: Authentiacate user

                user_id = message["id"]
                print("New connection at websocket " + str(ws) + " with id " + user_id)
                self.user_dict[user_id] = OnlineUser(user_id)
                out_msg = {
                    "type": "info",
                    "body": "Connected to game server."
                }
                await ws.send(json.dumps(out_msg))
            if (message["type"] == "enqueue"):
                if (self.user_dict[user_id].status == "IDLE"):
                    if (message["body"] == "duo"):
                        self.queue_duo.add_user(user_id)
                        self.user_dict[user_id].status = "QUEUEING"
                else:
                    out_msg = {
                        "type": "info",
                        "body": "Cannot queue for game, already in a queue or game."
                    }
                    await ws.send(json.dumps(out_msg))
            if (message["type"] == "gameInput"):
                if (self.user_dict[user_id].status == "PLAYING"):
                    player_lobby = self.user_dict[user_id].lobby_id
                    player_inputs = message["body"]
                    input_x = player_inputs["right"] - player_inputs["left"]
                    input_y = player_inputs["down"] - player_inputs["up"]
                    self.lobby_dict[player_lobby].relay_input(user_id, input_x, input_y)

            # Send outgoing messages
            if (self.user_dict[user_id].status == "PLAYING"):
                player_lobby = self.user_dict[user_id].lobby_id
                out_msg = {
                    "type": "gameState",
                    "body": self.lobby_dict[player_lobby].get_game_state(user_id)
                }
                await ws.send(json.dumps(out_msg))
            
        del self.user_dict[user_id]

    def start_matchmaking_duo(self):
        while(True):
            new_group = self.queue_duo.find_players()
            new_lobby = DuoLobby(new_group)
            self.lobby_dict[new_lobby.lobby_id] = new_lobby
            for uid in new_group:
                self.user_dict[uid].lobby_id = new_lobby.lobby_id

            lobby_thread = threading.Thread(target=new_lobby.run_match, daemon=True)
            lobby_thread.start()
            print("New lobby with id " + new_lobby.lobby_id + " started.")

            # TODO: remove lobby from dict when lobby ends


    def start_game_server(self):
        print("Starting server at port " + str(self.PORT))
        start_server = websockets.serve(self.on_message, "localhost", self.PORT)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

test_game_server = GameServer()
test_game_server.start_game_server()
