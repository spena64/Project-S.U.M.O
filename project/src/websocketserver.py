import asyncio
import json
import websockets
import threading
import os
from online_user import OnlineUser
from game_queue import GameQueue
from lobby import LobbyManager
from lobby import DuoLobby

class GameServer:
    def __init__(self):
        self.PORT = int(os.environ.get("PORT", 8080))
        self.user_dict = {}
        self.lobby_manager = LobbyManager(self.user_dict)

        self.queue_duo = GameQueue(self.user_dict, 2)

        mm_thread_duo = threading.Thread(target=self.start_matchmaking_duo, daemon=True)
        mm_thread_duo.start()

    async def on_message(self, ws, path):
        user_id = "unknown"

        while(True):
            try:
                # Process incoming messages
                message = await ws.recv()
                message = json.loads(message)

                if (message["type"] == "newConnection"):

                    # TODO: Authentiacate user

                    user_id = message["id"]
                    if (user_id in self.user_dict):
                        out_msg = {
                        "type": "info",
                        "body": "Already serving websocket for this user; closing connection."
                        }
                        await ws.send(json.dumps(out_msg))
                        return

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
                        player_inputs = message["body"]
                        input_x = player_inputs["right"] - player_inputs["left"]
                        input_y = player_inputs["down"] - player_inputs["up"]
                        self.lobby_manager.get_lobby_by_playerid(user_id).relay_input(user_id, input_x, input_y)

                # Send outgoing messages
                if (self.user_dict[user_id].status == "PLAYING"):
                    lobby = self.lobby_manager.get_lobby_by_playerid(user_id)
                    out_msg = {
                        "type": "gameState",
                        "body": lobby.get_game_state(user_id)
                    }
                    await ws.send(json.dumps(out_msg))
                    if (out_msg["body"]["matchData"]["state"] == "finished"):
                        lobby.remove_player(user_id)
                        self.user_dict[user_id].status = "IDLE"
                        self.user_dict[user_id].lobby_id = "none"
                        break
                
            except websockets.ConnectionClosed:
                break
            
        if (user_id in self.user_dict):
            if (self.user_dict[user_id].status == "QUEUEING"):
                self.queue_duo.remove_user()
            if (self.user_dict[user_id].status == "PLAYING"):
                lobby = self.lobby_manager.get_lobby_by_playerid(user_id)
                lobby.remove_player(user_id)
            del self.user_dict[user_id]
        print("Connection at websocket " + str(ws) + " closed, user " + user_id + " removed.")


    def start_matchmaking_duo(self):
        while(True):
            new_group = self.queue_duo.find_players()
            lobby_thread = threading.Thread(target=self.lobby_manager.host_duo_lobby, args=(new_group,), daemon=True)
            lobby_thread.start()

    def start_game_server(self):
        print("Starting server at port " + str(self.PORT))
        start_server = websockets.serve(self.on_message, host="0.0.0.0", port=self.PORT)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

test_game_server = GameServer()
test_game_server.start_game_server()
