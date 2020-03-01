class OnlineUser:
    def __init__(self, u_id):
        self.user_id = u_id
        # IDLE - connected to a websocket, but not in a queue or lobby
        # QUEUEING - waiting in a matchmaking queue
        # PLAYING - in a lobby
        self.status = "IDLE"
        self.lobby_id = "none"