from queue import Queue
import time

class GameQueue():
    def __init__(self, g_size):
        self.user_queue = Queue()
        self.group_size = g_size

    def add_user(self, user_id):
        self.user_queue.put(user_id)
        print("User " + user_id + " added to queue.")

    def grab_user(self):
        return self.user_queue.get()

    def collect_players(self, num_players):
        group = []
        for i in range(num_players):
            group.append(self.grab_user())
        return group

    def find_players(self):
        while(self.user_queue.qsize() < self.group_size):
            time.sleep(1)
        group = self.collect_players(self.group_size)
        return group


