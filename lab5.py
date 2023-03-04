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
#2a. Expand the function written in 1c to not accept anything other than a number, and only a number between 1 and 100.

def set_map_size(map_max_size):
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

def get_map_index(x, y, map_size, list):
    index = (x-1) * map_size + (y-1)
    return(index)

def get_map_value(x, y, map_size, list):
    index = (x-1) * map_size + (y-1)
    return(list[index])




#1d. Implement the agent number functionality. Write a separate function for this.
#2b. Expand the function written in 1d to only work when the size of the map is set and to not accept anything other than a number, and only a number between 1 and the number of cells. Since it is a square map, the number of cells is N * N, N being the length of one side of the square, as entered in 1e.

def how_many_agents(map_size, map):
    if map_size == 0:
        print("Set map size first")
        return
    else:
        while valid_input == 0:
            agents = input("How many agents do you want on the map?")
            if agents.isnumeric:
                agents = int(agents)
                if agents <= len(map):
                    valid_input = 1
                else:
                    print("Error: The map isn't big enough to hold that many agents!")    
            else:
                print("Error: Must be a number")
        return agents




#3a. Update the function written in 1a, so that after the user sets the map size (2a), a map is automatically generated (use 2a from Lab 4).






#3b. Update the function written in 1a, so that after the user sets the number of agents (2b), the map is updated so that all agents are added (use 4 from Lab 4).

def place_agents(map_size, map, agents):
    for i in agents:
        while success == 0:
            x = random.randint(1, map_size)
            y = random.randint(1, map_size)
            value = get_list_value(x, y, map_size, map)
            if value == 1:
                pass
            else:
                index = get_list_index(x, y, map_size, map)
                map[index] = 1
                success = 1
    return(map)



#4. Write a function to print the map, where zeroes are represented by "-" and ones by "X".

def print_map(map_size, map):
    for i in map:
        if map[i]:
            map[i] = "X"
        else:
            map[i] = "-"
    col = 0
    row = 0
    x = 0
    for row in range(map_size):
        for col in range(map_size):
            print(map[(col+x)], end="")    
        x = x + map_size
        print("")






#Main Program Loop
run = 1
map_size = 0
map_max_size = 100
map = []
agents = 0

while run == 1:
    print("Set (s)ize of the map")
    print("Set number of (a)gents")
    print("(G)enerate map")
    print("(P)rint map")
    print("(Q)uit")
    buffer = input("Select an option: ")
    if buffer == "q" or "Q":
        run = 0
    elif buffer == "s" or "S":
        map_size = set_map_size(map_max_size)
    elif buffer == "a" or "A":    
        agents = how_many_agents(map_size)
        map = generate_map(map_size)
        print_map(map_size, map)    
    elif buffer == "g" or "G":
        map = generate_map(map_size)
        print_map(map_size, map)
    elif buffer == "p" or "P":
        print_map(map_size, map)
    else:
        print("Error: Choose a valid option")
        print("")   