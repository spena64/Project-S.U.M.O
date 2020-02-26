from queue import Queue
import time

class GameQueue():
    def __init__(self):
        self.user_queue = Queue()
        self.group_size = 2

    def add_user(self, user_id):
        self.user_queue.put(user_id)

    def grab_user(self):
        return self.user_queue.get()

    def collect_players(self, num_players):
        group = []
        for i in range(num_players):
            group[i] = self.grab_user()
        return group

    def coordinate_lobbies(self):
        while(True):
            if (self.user_queue.qsize() >= self.group_size):
                group = self.collect_players(self.group_size)
                # Create a new lobby for these players
            time.sleep(1)
