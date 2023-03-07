#We want to get a program that presents a menu, allows us to change some settings, and can print a randomly generated map. The main menu should look something like this:

#Set (s)ize of the map
#Set number of (a)gents
#(G)enerate map
#(P)rint map
#(Q)uit

#If the user presses a s (or S), it should ask for the size of the map (assume a square map, so we just need the length of one side), and then return to the menu.
#If the user presses an a (or A), it should ask for the number of agents.
#If the user presses a p (or P), it should print a map, that looks like:

#-----XXXX------
#---XXX----XX--X
#--X----XX----X-
#----X------X---
#etc.

#If the user presses a q (or Q), it should exit the program.


#1a. Write a function that creates a loop with a set of menu options. Whatever the user presses, it should print the menu again.
#1b. Implement the quit functionality: if the user presses q or Q, it should exit the menu loop (and thus the program).
#1c. Implement the map size functionality. If the user presses s or S, ask for the size of the map. Write a separate function for this.
#1d. Implement the agent number functionality. Write a separate function for this.

#2a. Expand the function written in 1c to not accept anything other than a number, and only a number between 1 and 100.
#2b. Expand the function written in 1d to only work when the size of the map is set and to not accept anything other than a number, and only a number between 1 and the number of cells. Since it is a square map, the number of cells is N * N, N being the length of one side of the square, as entered in 1e.

#3a. Update the function written in 1a, so that after the user sets the map size (2a), a map is automatically generated (use 2a from Lab 4).
##3b. Update the function written in 1a, so that after the user sets the number of agents (2b), the map is updated so that all agents are added (use 4 from Lab 4).

4. Write a function to print the map, where zeroes are represented by "-" and ones by "X".

import random

run = 1
map_size = 0
map_max_size = 100
map = []
agents = 0
b = "z"   

def set_map_size(map_max_size):
    valid_input = 0
    while valid_input == 0:
        map_size = input("How big do you want the map to be? (1-{}): " .format(map_max_size))
        if map_size.isnumeric:
            map_size = int(map_size)
            if map_size not in range(1, map_max_size+1):
                print("Error: Choose a number between 1 and 100")
            else:
                valid_input = 1
        else:
            print("Error: Must be a number")
    return map_size


def generate_map(map_size): 
    map = []
    list_length = 0
    map_size = int(map_size)
    for list_length in range(map_size * map_size):
        #value = random.randint(0,1)
        value = 0
        map.append(value)
    return map


def how_many_agents(map_size, map):
    valid_input = 0
    if map_size == 0:
        print("Set map size first")
        return
    else:
        while valid_input == 0:
            agents = input("How many agents do you want on the map? ")
            if agents.isnumeric:
                agents = int(agents)
                if agents >= len(map):
                    valid_input = 1
                else:
                    print("Error: The map isn't big enough to hold that many agents!")    
            else:
                print("Error: Must be a number")
        return agents


def get_map_index(x, y, map_size, list):
    index = (x-1) * map_size + (y-1)
    return(index)


def place_agents(map_size, map, agents):
    for i in range(agents):
        success = 0
        while success == 0:
            x = random.randint(1, map_size)
            y = random.randint(1, map_size)
            index = get_map_index(x, y, map_size, map)
            if map[index] == 0:
                index = get_map_index(x, y, map_size, map)
                map[index] = 1
                success = 1
    return(map)


def print_map(map_size, map):
    col = 0
    row = 0
    x = 0
    for row in range(map_size):
        for col in range(map_size):
            if map[(col+x)] == 1:
                print("X", end="")
            else:
                print("-", end="")
        x = x + map_size
        print("")
  






#########Main Program Loop###########

while run == 1:
    print("Set (s)ize of the map")
    print("Set number of (a)gents")
    print("(G)enerate map")
    print("(P)rint map")
    print("(Q)uit")
    print("")
    b = input("Select an option: ")
    print("")
    if b.isalpha and len(b) == 1:
        if b == "s" or b == "S":
            map_size = set_map_size(map_max_size)
            print("")
            print("Map size set to {}" .format(map_size))
            print("")
            print("")    
        elif b == "a" or b == "A":
            agents = how_many_agents(map_size, map)
            print("")
        elif b == "g" or b == "G":
            map = generate_map(map_size)
            print("")
            print("Map generated...")
            map = place_agents(map_size, map, agents)
            print("")
            print("Agents placed")
            print_map(map_size, map)
            print("") 
        elif b == "p" or b == "P":
            print_map(map_size, map)
            print("")
        elif b == "q" or b == "Q":
            run = 0
        else:
            print("Error: Not a valid selection")
            print("")
    else:
        print("Error: not a valid selection")
        print("")
