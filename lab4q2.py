import random

gridsize = 5   # desired dimension for sides of a square grid of numbers
list = []   # stores our grid of numbers as a list of length n * n
x = 0   # x coordinate of desired cell
y = 0   # y coordinate of desired cell
index = -1  # index number in our list which contains the value in the cell at coordinates x, y
shouldchange = False # If True, 2b will modify value, if False, it will not
buffer = "" # input buffer
grid_max = 9  # maximum size of grid
run = 1  # Bool variable for main loop. While this is true, program will continue to run


#2a. Write a function that takes a parameter N and returns a list of zeroes of length N * N.
def make_grid_list(gridsize): 
    list = []
    list_length = 0
    gridsize = int(gridsize)
    for list_length in range(gridsize * gridsize):
        value = random.randint(0,1)
        list.append(value)
    return list

    # Function to display the grid (takes grid dimension and the list holding our grid)
def print_grid(gridsize, list):
    col = 0
    row = 0
    x = 0
    for row in range(gridsize):
        for col in range(gridsize):
            print(list[(col+x)], end=" ")    
        x = x + gridsize
        print("")



#2b. Write a function that takes as parameters an x and y value, and a list length N, and returns a list index as follows: i = (x-1) * N + (y-1).

def get_list_index(x, y, gridsize, list):
    i = (x-1) * gridsize + (y-1)
    return(i)



#2b. Write a function that takes a parameter L, which is a list of ones and zeroes, and parameters x and y representing coordinates, which returns the value of that point in the list, using 2b. Note that N is the square root of the length of the list. Test using a list generated in 2a.    

def get_list_value(x, y, gridsize, list):
    i = (x-1) * gridsize + (y-1)
    return(list[i])

#2c. Modify the function in 2b to print an error message on the screen when x or y is not within the range 1 to n.

#2d. Modify the function in 2d to take an additional boolean parameter, which if set, changes the value at the point in the list at (x,y). The default value of the parameter should be False, so that if you do not use it, it will by default not change the data.

def get_list_index_modify(x, y, gridsize, list, shouldchange):
    i = (x-1) * gridsize + (y-1)
    if shouldchange:
        list[i] = not list[i]
    return(i)

#3a. Write a function that takes a list and returns random x and y coordinates. The x and y coordinates have to be valid, given the length of the list.
#3b. Write a modification of 3a, returning only coordinates for a cell that has a zero value.

def rand_zero(gridsize, l):
    while list_value > 0:
        x = random.randint(1, grid_max)
        y = random.randint(1, grid_max)
        list_value = get_list_value(x, y, gridsize, list)
    return x, y

#4. Using all of the above, write a function that takes a list A, a list L, then finds a random position that is 0 in L, sets it to 1, and adds the (x,y) coordinates to A. A should be a list of dictionaries, where every item has a value "x" and a value "y".

def change_zero(gridsize, list_a, list):
    rz = rand_zero(gridsize)

while run:
    print("What would you like to do?")
    print("1: Create a new grid")
    print("2: Get the value of cell at an x, y coordinate")
    print("3: Quit")
    print("")
    b = input("?: ")

    if b.isnumeric():
        b = int(b)
        if b == 1:
            n = input("How big do you want your grid? ")
            n = int(n)
            l = make_grid_list(n)
            print("Here is your grid:")
            print_grid(n, l)
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
                y = input("Y coordinate?: ")
                y = int(y)
                i = get_list_index(x, y, n, l)
                print("") 
                print(l[i])
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
                y = input("Y coordinate?: ")
                y = int(y)
                i = get_list_index(x, y, n, l)
                print("") 
                print("The cell located at coordinates {}, {} is stored in the list at index number {} and contains the number {}." .format(x, y, i, l[i]))
                print("") 
                print("") 
        elif b == 3:
            run = 0

    else: 
        print("Error! Choose a number")
        print("")
        print("")
        print("")











"""
# MAIN PROGRAM LOOP
while run:
    print("What would you like to do?")
    print("1: Create a new grid")
    print("2: Get or change the value of cell at an x, y coordinate")
    print("3: Quit")
    print("")
    buffer = input("?: ")

    if buffer.isnumeric():
        buffer = int(buffer)
        if buffer == 1:
            gridsize = input("How big do you want your grid? (1-{}) " .format(grid_max))
            if not valid_value(grid_max, gridsize):
                gridsize = int(gridsize)
                pass
            else:    
                list = make_grid_list(gridsize)
                print("Here is your grid:")
                print_grid(gridsize, list)
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
                if not valid_value(grid_max, x):
                    pass
                else:
                    y = input("Y coordinate?: ")
                    if not valid_value(grid_max, y):
                        pass
                    else:
                        shouldchange = input("Do you want to change that cell? (y/n): ")
                        shouldchange = bool(shouldchange)
                        index = get_list_index_modify(x, y, gridsize, list, shouldchange)
                        if not valid_value(grid_max, x):
                            pass
                        else:
                            if shouldchange == False:
                                print("") 
                                print("The cell located at coordinates {}, {} is stored in the list at index number {} and contains the number {}." .format(x, y, index, list[index]))
                                print("")
                                print_grid(gridsize, list, index) 
                                print("")
                                print("")
                                print("and here is your grid displayed as a list:")
                                print("")
                                print(list)
                                print("")
                            else:
                                print("")
                                print("That cell has been modified.") 
                                print("")  
                                print("The cell located at coordinates {}, {} is stored in the list at index number {} and now contains the number {}." .format(x, y, index, list[index]))
                                print("")
                                print_grid(gridsize, list) 
                                print("")
                                print("")
                                print("and here is your grid displayed as a list:")
                                print("")
                                print(list)
                                print("")
        elif buffer == 3:
            run = 0

    else: 
        print("Error! Choose a number")
        print("")
        print("")
        print("")

"""




















