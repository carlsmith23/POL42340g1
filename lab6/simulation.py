from map import Map

class Simulation:
    def __init__(self):
        b = ""

    def main_loop(self):
        run = 1
        map = Map()
        while run == 1:
            print("Initialize (m)ap")
            print("(P)rint map")
            print("(Q)uit")
            print("")
            b = input("Select an option: ")
            print("")
            if b.isalpha and len(b) == 1:
                if b == "m" or b == "M":
                    map.generate()
                    map.place_agents()
                    map.display()
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