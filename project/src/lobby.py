from match import Match

class Lobby():
    def __init__(self):
        self.lobby_id = "" # TODO: generate random hash
        # WAITING - waiting for players to join / ready up
        # STARTED - matches are being played
        # FINISHED - all matches have completed
        self.status = "WAITING"

class DuoLobby(Lobby):
    def __init__(self, player_ids):
        super().__init__(self)
        self.player_1_id = player_ids[0]
        self.player_2_id = player_ids[1]
        self.match = Match()
        self.match.add_player(self.player_1_id, [300, 500], 1, 30, 1)
        self.match.add_player(self.player_2_id, [700, 500], 1, 30, 1)

    def relay_input(self, user_id, input_x, input_y):
        self.match.set_player_input(user_id, input_x, input_y)

    def play(self):
        self.status = "STARTED"
        self.match.run_game_loop()
        self.status = "FINISHED"

    def get_game_state(self, user_id):
        game_state = {
            "playerNames": [self.player_1_id, self.player_2_id],  # TODO change these to reference usernames
            "matchData": self.match.get_match_data(user_id),
            "playerData": self.match.get_player_data()
        }
        return game_state

class LobbyManager():
    def __init__(self, u_dict):
        self.lobby_dict = {}
        self.user_dict = u_dict

    def host_duo_lobby(self, players):
        new_lobby = DuoLobby(players)
        self.lobby_dict[new_lobby.lobby_id] = new_lobby
        for uid in players:
            self.user_dict[uid].lobby_id = new_lobby.lobby_id

        print("New lobby with id " + new_lobby.lobby_id + " started.")
        new_lobby.play()

        # Possibly test for rematch?

        del self.lobby_dict[new_lobby.lobby_id]
        for uid in players:
            self.user_dict[uid].lobby_id = "none"
            self.user_dict[uid].status = "IDLE"

    def get_lobby_by_playerid(self, user_id):
        return self.lobby_dict[self.user_dict[user_id].lobby_id]