#2a. Write a function that takes a parameter N and returns a list of zeroes of length N * N.

#2b. Write a function that takes as parameters an x and y value, and a list length N, and returns a list index as follows: i = (x-1) * N + (y-1).

import random
from colorama import Fore, Style

# Create a square grid of arbitrary size filled with random 1s and 0s, store it in a list, and display it as a grid. Take an x coordinate and a y coordinate and return the position in the list where the grid cell at those coordinates is stored.

gridsize = 5   # desired dimension for sides of a square grid of numbers
list = []   # stores our grid of numbers as a list of length n * n
x = 0   # x coordinate of desired cell
y = 0   # y coordinate of desired cell
index = -1  # index number in our list which contains the value in the cell at coordinates x, y
buffer = "" # input buffer
grid_max = 9  # maximum size of grid
run = 1  # Bool variable for main loop. While this is true, program will continue to run

#Function to create the grid (takes the desired dimension of our grid)
def make_grid_list(gridsize): 
    list = []
    list_length = 0
    for list_length in range(gridsize * gridsize):
        value = random.randint(0,1)
        list.append(value)
    return list

#Function to display the grid (takes grid dimension and the list holding our grid)
def print_grid(gridsize, list):
    col = 0
    row = 0
    x = 0
    for row in range(gridsize):
        for col in range(gridsize):
            print(list[(col+x)], end=" ")    
        x = x + gridsize
        print("")

def print_grid_highlight(gridsize, list, index):
    col = 0
    row = 0
    x = 0
    for row in range(gridsize):
        for col in range(gridsize):
            if (col+x) == index:
                print(Fore.RED + "{}" .format(list[(col+x)]) + Style.RESET_ALL, end=" ")
            else:
                print(list[(col+x)], end=" ")    
        x = x + gridsize
        print("")

#Function to display the grid (takes grid dimension and the list holding our grid)
def print_grid_w_colrow(gridsize, list, index):
    col = 0
    row = 0
    x = 0
    print(" X", end=" ")
    for col_heading in range(gridsize):
        print(Fore.LIGHTBLUE_EX + "{}" .format(str(col_heading + 1)) + Style.RESET_ALL, end=" ")
    print("")    
    print("Y")        
    for row in range(gridsize):
        print(Fore.LIGHTBLUE_EX + "{}" .format(str(row + 1)) + Style.RESET_ALL, end="  ")
        for col in range(gridsize):
            if (col+x) == index:
                print(Fore.RED + "{}" .format(list[(col+x)]) + Style.RESET_ALL, end=" ")
            else:
                print(list[(col+x)], end=" ")
        x = x + gridsize    
        print("")

def print_grid_over_9x9(gridsize, list):
    col = 0
    row = 0
    x = 0
    col_heading = 0

    print("    X", end="")
    for col_heading in range(gridsize):
        print(col_heading + 1, end="")
        if col_heading < 9:
            print(" ", end="")
        if gridsize > 10:
                print(" ", end="")
    print("")
    if gridsize > 10:
        print("")
    print("Y")        
    for row in range(gridsize):
        print(row + 1, end="   ")
        if row < 9:
            print(" ", end="")
        for col in range(gridsize):
            print(list[(col+x)], end=" ")
            if gridsize > 10:
                print(" ", end="")    
        x = x + gridsize
        print("")
        if gridsize > 10:
            print("")
        
#Function to get list index number from grid x and y coordinates (takes the desired x and y coordinates as well as the dimension of our grid and the list holding it)
def get_list_index(x, y, gridsize, list):
    i = (x-1) * gridsize + (y-1)
    return(i)

#Function to get list index number from grid x and y coordinates (takes the desired x and y coordinates as well as the dimension of our grid and the list holding it). Fixed so x is horizontal and y is vertical.
def get_list_index_fixed(x, y, gridsize, list):
    index = (y-1) * gridsize + (x-1)
    return(index)

#Takes a value and returns true if value is between 1 and the max you have set, print's error and returns false if it is not.
def validate_value(grid_max, gridsize):
    if gridsize in range(1, (grid_max+1)):
        return True
    else:
        print("Error: Must be a number between 1 and {}" .format(grid_max))
        print("")
        return False


# MAIN PROGRAM LOOP
while run:
    print("What would you like to do?")
    print("1: Create a new grid")
    print("2: Get the value of cell at an x, y coordinate")
    print("3: Quit")
    print("")
    buffer = input("?: ")

    if buffer.isnumeric():
        buffer = int(buffer)
        if buffer == 1:
            gridsize = input("How big do you want your grid? (1-{}) " .format(grid_max))
            gridsize = int(gridsize)
            if not validate_value(grid_max, gridsize):
                pass
            else:    
                list = make_grid_list(gridsize)
                print("Here is your grid:")
                print_grid_w_colrow(gridsize, list, index)
                print("")
                print("and here is your grid displayed as a list:")
                print(list)
                print("")
                print("")
                
        elif buffer == 2:
            if len(list) == 0:
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
                        index = get_list_index(x, y, gridsize, list)
                        print("") 
                        print("The cell located at coordinates {}, {} is stored in the list at index number {} and contains the number {}." .format(x, y, index, list[index]))
                        print("")
                        print_grid_fancy(gridsize, list, index) 
                        print("")
                        print("")
                        print("and here is your grid displayed as a list:")
                        print("")
                        print("[", end = "")
                        for z in range(0, index):
                            print(list[z], end = ", ")
                        print(Fore.RED + "{}" .format(list[index]) + Style.RESET_ALL, end=", ")
                        for z in range(index, (gridsize*gridsize)):    
                            print(list[z], end = ", ")
                        print("]")
                        print("")    
        elif buffer == 3:
            run = 0

    else: 
        print("Error! Choose a number")
        print("")
        print("")
        print("")






#2b. Write a function that takes a parameter L, which is a list of ones and zeroes, and parameters x and y representing coordinates, which returns the value of that point in the list, using 2b. Note that N is the square root of the length of the list. Test using a list generated in 2a.















#2c. Modify the function in 2b to print an error message on the screen when x or y is not within the range 1 to n.
#2d. Modify the function in 2d to take an additional boolean parameter, which if set, changes the value at the point in the list at (x,y). The default value of the parameter should be False, so that if you do not use it, it will by default not change the data.