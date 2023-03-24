from config import Config
from map import Map

class Menu:
    def __init__(self):
        self.b = ""     #menu input buffer
        self.size = ""  #size to pass to map object

    def main_loop(self):
        run = 1
        config = Config() #creating config object
        map = Map(config.get_max()) #creating map object

########MAIN MENU STARTS HERE##########
        while run == 1:
            print("Initialize (m)ap")
            print("(P)rint map")
            print("(Q)uit")
            print("")
            self.b = input("Select an option: ")
            print("")
            if self.b is not None and self.b.isalpha:

                ###MAP MENU###
                if self.b == "m" or self.b == "M":
                    valid_input = 0
                    while valid_input == 0:
                        self.size = input("How big do you want the map to be? (1-{}): " .format(config.get_max()))
                        if self.size.isnumeric():
                            self.size = int(self.size)
                            if self.size in range(1, config.get_max() + 1):
                                print("")
                                print("Map size set to {}" .format(self.size))
                                print("")
                                map.generate(self.size) #Generates map as list of length size*size
                                print("Map generated")
                                print("")
                                valid_input = 1
                            else:
                                print("Error: Choose a number between 1 and 100")
                        else:
                            print("Error: Must be a number")

                    ###After map is generated, automatically configure and place agents
                    valid_input = 0
                    if self.size == 0:
                        print("Set map size first")
                        return
                    else:
                        while valid_input == 0:
                            self.agents = input("How many agents do you want on the map? ")
                            if self.agents is not None and self.agents.isnumeric():
                                self.agents = int(self.agents)
                                if self.agents <= map.get_length():
                                    map.place_agents(self.agents) #Randomly places agents in empty cells
                                    print("")
                                    print("{} agents placed on the map" .format(self.agents))
                                    print("")                  
                                    valid_input = 1

                                else:
                                    print("Error: The map isn't big enough to hold that many agents!")

                            else:
                                print("Error: Must be a number")
                    map.display() #display current map with agents

                ###PRINT MAP MENU
                elif self.b == "p" or self.b == "P":
                    if self.size is None:    
                        map.display() #display current map with agents
                    else:
                        print("Error: Generate map first")
                        print("")
                ##QQUIT    
                elif self.b == "q" or self.b == "Q":
                    run = 0

                else:
                    print("")
                    print("Error: Not a valid selection")
                    print("")

            else:
                print("")
                print("Error: not a valid selection")
                print("")    