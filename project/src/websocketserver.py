import asyncio
import json
import websockets
import threading
import match

class GameServer:
    def __init__(self):
        self.PORT = 8081

        self.test_match = match.Match()
        self.match_thread = threading.Thread(target=self.test_match.run_game_loop, daemon=True)
        self.is_match_started = False
        print("Creating new game server.")

    async def on_message(self, ws, path):
        user_id = ""
        while(True):
            message = await ws.recv()
            message = json.loads(message)

            if (message["type"] == "newConnection"):
                user_id = message["id"]
                if (self.is_match_started == False):
                    self.test_match.add_player(user_id, [400, 500], 0.25, 30, 1)
                    print("New connection at websocket " + str(ws) + " with id " + user_id)
                    out_msg = {
                        "type": "info",
                        "body": "Joined match."
                    }
                    await ws.send(json.dumps(out_msg))
                else:
                    out_msg = {
                        "type": "info",
                        "body": "Match already started, cannot join."
                    }
                    await ws.send(json.dumps(out_msg))
                    return
            if (message["type"] == "startMatch" and self.is_match_started == False):
                self.is_match_started = True
                print("Started match.")
                self.match_thread.start()
            if (message["type"] == "gameInput"):
                player_inputs = message["body"]
                input_x = player_inputs["right"] - player_inputs["left"]
                input_y = player_inputs["down"] - player_inputs["up"]
                self.test_match.set_player_input(user_id, input_x, input_y)

            # Send player data to client
            out_data = {
                "type": "gameState",
                "matchState": self.test_match.get_match_data(),
                "body": self.test_match.get_player_data()
            }
            if (out_data["matchState"]["winner"] == user_id):
                out_data["matchState"]["youWin"] = True
            await ws.send(json.dumps(out_data))
            
            if (out_data["matchState"]["state"] == "finished"):
                break

    def start_game_server(self):
        print("Starting server at port " + str(self.PORT))
        start_server = websockets.serve(self.on_message, "localhost", self.PORT)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

test_game_server = GameServer()
test_game_server.start_game_server()
