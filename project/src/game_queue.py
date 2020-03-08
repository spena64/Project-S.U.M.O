from queue import Queue
import time

class GameQueue():
    def __init__(self, u_dict, g_size):
        self.user_queue = Queue()
        self.size = 0
        self.user_dict = u_dict
        self.group_size = g_size

    def add_user(self, user_id):
        self.user_queue.put(user_id)
        self.size += 1
        print("User " + user_id + " added to queue.")

        print("Queue size: " + str(self.size))

    def grab_user(self):
        user = self.user_queue.get()
        self.size -= 1

        print("Queue size: " + str(self.size))

        while (user not in self.user_dict or self.user_dict[user].status != "QUEUEING"):
            print("Tried to pull invalid user from matchmaking queue.")
            user = self.user_queue.get()

        return user

    def remove_user(self):
        self.size -= 1

        print("Queue size: " + str(self.size))

    def collect_players(self, num_players):
        group = []
        for i in range(num_players):
            group.append(self.grab_user())
        return group

    def find_players(self):
        while(self.size < self.group_size):
            time.sleep(1)
        group = self.collect_players(self.group_size)
        return group


