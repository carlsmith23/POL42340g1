#1a. Take the infectious disease simulation from the previous homework and write a function that runs the simulation R times, returning a list with all the results.
#1b. Use the library matplotlib to produce a histogram of the simulation results, explained at the top of https://datatofish.com/plot-histogram-python/

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

#2a. Write a function that takes a parameter N and returns a list of zeroes of length N * N.
#2b. Write a function that takes as parameters an x and y value, and a list length N, and returns a list index as follows: i = (x-1) * N + (y-1).
#2b. Write a function that takes a parameter L, which is a list of ones and zeroes, and parameters x and y representing coordinates, which returns the value of that point in the list, using 2b. Note that N is the square root of the length of the list. Test using a list generated in 2a.
#2c. Modify the function in 2b to print an error message on the screen when x or y is not within the range 1 to n.
#2d. Modify the function in 2d to take an additional boolean parameter, which if set, changes the value at the point in the list at (x,y). The default value of the parameter should be False, so that if you do not use it, it will by default not change the data.



#3a. Write a function that takes a list and returns random x and y coordinates. The x and y coordinates have to be valid, given the length of the list.
#3b. Write a modification of 3a, returning only coordinates for a cell that has a zero value.



#4. Using all of the above, write a function that takes a list A, a list L, then finds a random position that is 0 in L, sets it to 1, and adds the (x,y) coordinates to A. A should be a list of dictionaries, where every item has a value "x" and a value "y".