from config import Config
from map import Map

class Simulation:
    def __init__(self):
        self.b = ""

    def main_loop(self):
        run = 1
        config = Config()
        map = Map(config.get_max())
        while run == 1:
            print("Initialize (m)ap")
            print("(P)rint map")
            print("(Q)uit")
            print("")
            self.b = input("Select an option: ")
            print("")
            if self.b is not none and self.b.isalpha:
                if self.b == "m" or self.b == "M":
                    map.generate()
                    map.place_agents()
                    map.display()
                elif self.b == "p" or self.b == "P":
                    map.display()
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