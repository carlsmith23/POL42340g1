#1a. Take the infectious disease simulation from the previous homework and write a function that runs the simulation R times, returning a list with all the results.
#1b. Use the library matplotlib to produce a histogram of the simulation results, explained at the top of https://datatofish.com/plot-histogram-python/
"""
import random
import matplotlib.pyplot

initial_infected = 1
time_to_run = 100
chance_of_cure = 15
chance_of_spread = 25
n_times = 100
list = ""
def infected_person(cure, spread):
    randomizer = 0
    randomizer = random.randint(1,100)
    if randomizer in range(1, cure):
        return "cured"
    elif randomizer in range((100 - spread), 100):
        return "spreads" 
    else: 
        return
   

def time_period(infected, cure, spread):
        tested = 0
        while tested < infected:
            condition = infected_person(cure, spread)
            if condition == "cured":
                infected += -1
            elif condition == "spreads":
                infected += 1
            tested += 1
        return infected


def iterate_time(infected, time, cure, spread):
    time_past = 0
    while time_past < time:
        infected = time_period(infected, cure, spread)
        time_past += 1
    return infected


def repeat_simulation(n_times, initial_infected, time_to_run, chance_of_cure, chance_of_spread):
    round = 0
    new_infected = 0
    infected_list = []
    while round <= n_times:
        new_infected = iterate_time(initial_infected, time_to_run, chance_of_cure, chance_of_spread)

        print("Round {}: {} infected people." .format(round, new_infected)) 

        infected_list.append(new_infected)
        round += 1
    return infected_list    

list = repeat_simulation(n_times, initial_infected, time_to_run, chance_of_cure, chance_of_spread)

print(list)


matplotlib.pyplot.hist(list, bins='auto')
matplotlib.pyplot.show()
"""

#2a. Write a function that takes a parameter N and returns a list of zeroes of length N * N.









#2b. Write a function that takes as parameters an x and y value, and a list length N, and returns a list index as follows: i = (x-1) * N + (y-1).


import random
from colorama import Fore, Style

# Create a square grid of arbitrary size filled with random 1s and 0s, store it in a list, and display it as a grid. Take an x coordinate and a y coordinate and return the position in the list where the grid cell at those coordinates is stored.

n = 5  # desired dimension for sides of a square grid of numbers
l = [] # stores our grid of numbers as a list of length n * n
x = 0  # x coordinate of desired cell
y = 0  # y coordinate of desired cell
i = -1  # index number in our list which contains the value in the cell at coordinates x, y
b = "" # input buffer
grid_max = 9  # maximum size of grid
r = 1  # Bool variable for main loop. While this is true, program will continue to run

#Function to create the grid (takes the desired dimension of our grid)
def make_grid_list(n): 
    list = []
    list_length = 0
    for list_length in range(n * n):
        value = random.randint(0,9)
        list.append(value)
    return list

#Function to display the grid (takes grid dimension and the list holding our grid)
def print_grid(n, l):
    col = 0
    row = 0
    x = 0
    for row in range(n):
        for col in range(n):
            print(l[(col+x)], end=" ")    
        x = x + n
        print("")

def print_grid_highlight(n, l, i):
    col = 0
    row = 0
    x = 0
    for row in range(n):
        for col in range(n):
            if (col+x) == i:
                print(Fore.RED + "{}" .format(l[(col+x)]) + Style.RESET_ALL, end=" ")
            else:
                print(l[(col+x)], end=" ")    
        x = x + n
        print("")

#Function to display the grid (takes grid dimension and the list holding our grid)
def print_grid_fancy(n, l, i):
    col = 0
    row = 0
    x = 0
    print(" X", end=" ")
    for col_heading in range(n):
        print(Fore.LIGHTBLUE_EX + "{}" .format(str(col_heading + 1)) + Style.RESET_ALL, end=" ")
    print("")    
    print("Y")        
    for row in range(n):
        print(Fore.LIGHTBLUE_EX + "{}" .format(str(row + 1)) + Style.RESET_ALL, end="  ")
        for col in range(n):
            if (col+x) == i:
                print(Fore.RED + "{}" .format(l[(col+x)]) + Style.RESET_ALL, end=" ")
            else:
                print(l[(col+x)], end=" ")
        x = x + n    
        print("")

def print_grid_extra_fancy(n, l):
    col = 0
    row = 0
    x = 0
    col_heading = 0

    print("    X", end="")
    for col_heading in range(n):
        print(col_heading + 1, end="")
        if col_heading < 9:
            print(" ", end="")
        if n > 10:
                print(" ", end="")
    print("")
    if n > 10:
        print("")
    print("Y")        
    for row in range(n):
        print(row + 1, end="   ")
        if row < 9:
            print(" ", end="")
        for col in range(n):
            print(l[(col+x)], end=" ")
            if n > 10:
                print(" ", end="")    
        x = x + n
        print("")
        if n > 10:
            print("")
        
#Function to get list index number from grid x and y coordinates (takes the desired x and y coordinates as well as the dimension of our grid and the list holding it)
def get_list_index(x, y, n, l):
    i = (x-1) * n + (y-1)
    return(i)

def get_list_index_fixed(x, y, n, l):
    i = (y-1) * n + (x-1)
    return(i)



def validate_value(grid_max, n):
    if n in range(1, (grid_max+1)):
        return True
    else:
        print("Error: Must be a number between 1 and {}" .format(grid_max))
        print("")
        return False


# MAIN PROGRAM LOOP
while r:
    print("What would you like to do?")
    print("1: Create a new grid")
    print("2: Get the value of cell at an x, y coordinate")
    print("3: Quit")
    print("")
    b = input("?: ")

    if b.isnumeric():
        b = int(b)
        if b == 1:
            n = input("How big do you want your grid? (1-{}) " .format(grid_max))
            n = int(n)
            if not validate_value(grid_max, n):
                pass
            else:    
                l = make_grid_list(n)
                print("Here is your grid:")
                print_grid_fancy(n, l, i)
                print("")
                print("and here is your grid displayed as a list:")
                print(l)
                print("")
                print("")
                
        elif b == 2:
            if len(l) == 0:
                print("Error: you must first create a grid")
                print("")
                print("") 
            else: 
                x = input("X coordinate?: ")
                x = int(x)
                if not validate_value(grid_max, x):
                    pass
                else:
                    y = input("Y coordinate?: ")
                    y = int(y)
                    if not validate_value(grid_max, y):
                        pass
                    else:
                        i = get_list_index(x, y, n, l)
                        print("") 
                        print("The cell located at coordinates {}, {} is stored in the list at index number {} and contains the number {}." .format(x, y, i, l[i]))
                        print("")
                        print_grid_fancy(n, l, i) 
                        print("")
                        print("")
                        print("and here is your grid displayed as a list:")
                        print("")
                        print("[", end = "")
                        for z in range(0, i):
                            print(l[z], end = ", ")
                        print(Fore.RED + "{}" .format(l[i]) + Style.RESET_ALL, end=", ")
                        for z in range(i, (n*n)):    
                            print(l[z], end = ", ")
                        print("]")
                        print("")    
        elif b == 3:
            r = 0

    else: 
        print("Error! Choose a number")
        print("")
        print("")
        print("")






#2b. Write a function that takes a parameter L, which is a list of ones and zeroes, and parameters x and y representing coordinates, which returns the value of that point in the list, using 2b. Note that N is the square root of the length of the list. Test using a list generated in 2a.















#2c. Modify the function in 2b to print an error message on the screen when x or y is not within the range 1 to n.
#2d. Modify the function in 2d to take an additional boolean parameter, which if set, changes the value at the point in the list at (x,y). The default value of the parameter should be False, so that if you do not use it, it will by default not change the data.



#3a. Write a function that takes a list and returns random x and y coordinates. The x and y coordinates have to be valid, given the length of the list.
#3b. Write a modification of 3a, returning only coordinates for a cell that has a zero value.



#4. Using all of the above, write a function that takes a list A, a list L, then finds a random position that is 0 in L, sets it to 1, and adds the (x,y) coordinates to A. A should be a list of dictionaries, where every item has a value "x" and a value "y".