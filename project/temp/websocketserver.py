import asyncio
import json
import websockets

async def get_message(ws, path):
    while(True):
        message = await ws.recv()
        message = json.loads(message)

        if (message["type"] == "newConnection"):
            # Create new match
        
            outMsg = json.dumps({
                "type": "test",
                "body": "Connected."
            }) 
            await ws.send(outMsg)
        if (message["type"] == "gameInput"):
            # Relay input
            print(message)
            

start_server = websockets.serve(get_message, "localhost", 8081)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()