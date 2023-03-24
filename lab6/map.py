import random

class Map:
    def __init__(self, max_size):
        self.size = "size"
        self.max_size = max_size
        self.agents = "agents"
        self.list = []


    def generate(self):
        valid_input = 0
        while valid_input == 0:
            self.size = input("How big do you want the map to be? (1-{}): " .format(self.max_size))
            if self.size.isnumeric():
                self.size = int(self.size)
                if self.size in range(1, self.max_size + 1):
                    print("")
                    print("Map size set to {}" .format(self.size))
                    print("")
                    self.list = []
                    for list_length in range((self.size * self.size) + 1):
                        self.list.append(0)
                    print("")
                    print("Map generated")
                    print("")
                    valid_input = 1
                else:
                    print("Error: Choose a number between 1 and 100")
            else:
                print("Error: Must be a number")


    def place_agents(self):
        valid_input = 0
        if self.size == 0:
            print("Set map size first")
            return
        else:
            while valid_input == 0:
                self.agents = input("How many agents do you want on the map? ")
                if self.agents.isnumeric():
                    self.agents = int(self.agents)
                    if self.agents <= len(self.list):
                        print("")
                        print("{} agents" .format(self.agents))
                        print("")
                        for i in range(self.agents):
                            index = 0
                            success = 0
                            while success == 0:
                                index = random.randint(1, (self.size * self.size))
                                if self.list[index] == 0:
                                    self.list[index] = 1
                                    success = 1
                        print("")
                        print("{} agents placed on the map" .format(self.agents))
                        print("")                   
                        valid_input = 1
                    else:
                        print("Error: The map isn't big enough to hold that many agents!")    
                else:
                    print("Error: Must be a number")


    def get_index(self, x, y):
        index = (x-1) * self.size + (y-1)
        return(index)


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