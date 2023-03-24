import random

class Map:
    def __init__(self, max_size):
        self.size = "size"
        self.max_size = max_size
        self.agents = "agents"
        self.list = []


    def generate(self, size):
        self.size = size
        for list_length in range((self.size * self.size) + 1):
            self.list.append(0)


    def place_agents(self, agents):
        self.agents = agents
        for i in range(self.agents):
            index = 0
            success = 0
            while success == 0:
                index = random.randint(1, (self.size * self.size))
                if self.list[index] == 0:
                    self.list[index] = 1
                    success = 1


    def get_index(self, x, y):
        index = (x-1) * self.size + (y-1)
        return(index)
    

    def get_length(self):
        return len(self.list)


    def display(self):
        col = 0
        row = 0
        x = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.list[(col+x)] == 1:
                    print("X", end="")
                else:
                    print("-", end="")
            x = x + self.size
            print("")