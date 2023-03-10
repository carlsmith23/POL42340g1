from map import Map

class Simulation:
    def __init__(self):
        b = ""

    def main_loop(self):
        run = 1
        map = Map()
        while run == 1:
            print("Set (s)ize of the map")
            print("Set number of (a)gents")
            print("(P)rint map")
            print("(Q)uit")
            print("")
            b = input("Select an option: ")
            print("")
            if b.isalpha and len(b) == 1:
                if b == "s" or b == "S":
                    map.generate()
                elif b == "a" or b == "A":
                    map.place_agents()
                elif b == "p" or b == "P":
                    map.display()
                elif b == "q" or b == "Q":
                    run = 0
                else:
                    print("")
                    print("Error: Not a valid selection")
                    print("")
            else:
                print("")
                print("Error: not a valid selection")
                print("")    