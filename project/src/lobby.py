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

    def run_match(self):
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
