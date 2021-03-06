import time
import math
import random

RING_CENTER_X = 700
RING_CENTER_Y = 500
RING_RADIUS = 450

class Match:
    def __init__(self):
        self.player_dict = {}
        self.state = "waiting"
        self.winner = "Undecided"
        self.color_set = ["#C21212", "#EA8015", "#EAbB15", "#69880D", "#43B911", "#13D78D", "#10D3EF", "#096ACC", "#9553D7", "#F971D7"]
        self.num_players = 2

    def add_player(self, user_id, position, acceleration_rate, radius, mass):
        color = self.color_set.pop(random.randint(0, len(self.color_set) - 1))
        self.player_dict[user_id] = Player(position, acceleration_rate, radius, mass, color)

    def run_game_loop(self):
        # Game loop
        self.state = "started"
        while(self.num_players > 1):
            in_ring_num = 0
            for id in self.player_dict:
                player = self.player_dict[id]
                player.move()

                for other_id in self.player_dict:
                    player.check_collision(self.player_dict[other_id])

                if (player.is_in_bounds()):
                    in_ring_num += 1
            
            if (in_ring_num == 1):
                break
            time.sleep(0.01)
        self.end_match()

    def end_match(self):
        self.state = "finished"
        for id in self.player_dict:
            player = self.player_dict[id]
            if (player.is_in_bounds()):
                self.winner = id

    def get_match_data(self, user_id):
        match_data = {
            "state": self.state,
            "winner": self.winner,
            "youWin": False
        }
        if (match_data["winner"] == user_id):
            match_data["youWin"] = True
        return match_data

    def get_player_state(self, user_id):
        player_state = {
            "x": self.player_dict[user_id].get_position()[0],
            "y": self.player_dict[user_id].get_position()[1],
            "radius": self.player_dict[user_id].get_radius(),
            "color": self.player_dict[user_id].get_color()
        }
        return player_state

    def get_player_data(self):
        player_data = {}
        for id in self.player_dict:
            player_data[id] = self.get_player_state(id)
        return player_data

    def set_player_input(self, user_id, input_x, input_y):
        direction_vector = self.normalize_input(input_x, input_y)
        self.player_dict[user_id].set_direction(direction_vector)
        return

    @staticmethod
    def normalize_input(x, y):
        magnitude = math.sqrt(x ** 2 + y ** 2)
        if (magnitude == 0):
            return [0, 0]
        
        return [x / magnitude, y / magnitude]
    
class Player:
    def __init__(self, position, acceleration_rate, radius, mass, color):
        self.position = position
        self.speed = [0, 0]
        self.direction = [0, 0]
        self.acceleration_rate = acceleration_rate
        self.radius = radius
        self.mass = mass
        self.color = color
        self.drag = 1.01
        self.is_alive = True
    
    def get_position(self):
        return self.position

    def get_speed(self):
        return self.speed

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_color(self):
        return self.color

    def move(self):
        self.speed[0] += self.direction[0] * self.acceleration_rate
        self.speed[1] += self.direction[1] * self.acceleration_rate

        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        self.speed[0] /= self.drag
        self.speed[1] /= self.drag

        # Stopping speed
        if (abs(self.speed[0]) < 0.01):
            self.speed[0] = 0
        if (abs(self.speed[1]) < 0.01):
            self.speed[1] = 0

        # Kill movement if out of bounds
        self.is_alive = math.sqrt( (self.position[0] - RING_CENTER_X) ** 2 + (self.position[1] - RING_CENTER_Y) ** 2 ) < RING_RADIUS
        if (self.is_alive == False):
            self.direction = [0, 0]
        return

    def set_direction(self, direction_vector):
        if (self.is_alive == True):
            self.direction = direction_vector
        return

    def check_collision(self, other_player):
        # We do not need to check collisions against ourself
        if (other_player == self):
            return

        other_pos = other_player.get_position()
        other_radius = other_player.get_radius()

        displacement_x = self.position[0] - other_pos[0]
        displacement_y = self.position[1] - other_pos[1]
        distance = math.sqrt(displacement_x ** 2 + displacement_y ** 2)
        if (distance < self.radius + other_radius):
            other_speed = math.sqrt(other_player.get_speed()[0] ** 2 + other_player.get_speed()[1] ** 2)
            self.collide(other_speed, displacement_x, displacement_y)

    def collide(self, other_speed, displacement_x, displacement_y):
        disp_vector = Match.normalize_input(displacement_x, displacement_y)
        self.position[0] -= disp_vector[0] * 0.1
        self.position[1] -= disp_vector[1] * 0.1

        self.speed[0] += disp_vector[0] * other_speed * 0.5
        self.speed[1] += disp_vector[1] * other_speed * 0.5

    def is_in_bounds(self):
        return self.is_alive

