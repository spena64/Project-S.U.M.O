from match import Match
import random
import string
import threading
import time

class Lobby():
    def __init__(self):
        self.lobby_id = "".join([random.choice(string.ascii_letters + string.digits) for n in range(8)])
        # WAITING - waiting for players to join / ready up
        # STARTED - matches are being played
        # FINISHED - all matches have completed
        self.status = "WAITING"

class DuoLobby(Lobby):
    def __init__(self, player_ids):
        super().__init__()
        self.player_1_id = player_ids[0]
        self.player_2_id = player_ids[1]
        self.match = Match()
        self.match.add_player(self.player_1_id, [300, 500], 0.25, 30, 1)
        self.match.add_player(self.player_2_id, [700, 500], 0.25, 30, 1)
        self.num_players = 2

    def relay_input(self, user_id, input_x, input_y):
        self.match.set_player_input(user_id, input_x, input_y)

    def play(self):
        self.status = "STARTED"
        self.match.run_game_loop()
        # Wait for all players to leave
        while (self.num_players > 0):
            pass
        self.status = "FINISHED"

    def get_game_state(self, user_id):
        game_state = {
            "playerNames": [self.player_1_id, self.player_2_id],  # TODO change these to reference usernames
            "matchData": self.match.get_match_data(user_id),
            "playerData": self.match.get_player_data()
        }
        return game_state

    def remove_player(self, user_id):
        self.num_players -= 1
        self.match.num_players -= 1

class LobbyManager():
    def __init__(self, u_dict):
        self.lobby_dict = {}
        self.user_dict = u_dict

    def host_duo_lobby(self, players):
        new_lobby = DuoLobby(players)
        l_id = new_lobby.lobby_id
        self.lobby_dict[l_id] = new_lobby
        for uid in players:
            self.user_dict[uid].lobby_id = l_id
            self.user_dict[uid].status = "PLAYING"

        print("New lobby with id " + l_id + " started.")
        new_lobby.play()

        print("Lobby " + l_id + " finished.")
        del self.lobby_dict[l_id]

    def get_lobby_by_playerid(self, user_id):
        return self.lobby_dict[self.user_dict[user_id].lobby_id]