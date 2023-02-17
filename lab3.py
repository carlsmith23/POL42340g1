#NOTE: for all these exercises, only use while-loops (or recursion), not for-loops. Where you can use functions you wrote in earlier exercises, you should always do so.

#1.  Write a function with parameters N, R, and K, that throws N dice R times and returns what proportion of results the sum of the N dice is exactly K.
import random
k = 100
how_many_dice = 30
how_many_groups = 300

def roll_dice():
    dice = 0
    dice = random.randint(1, 6)
    print(dice)
    return dice

def roll_group(how_many_dice):
    dice_rolled = 0
    total = 0
    while dice_rolled < how_many_dice:
        total = total + roll_dice()
        dice_rolled += 1
    print("")
    print("Group total: ", total)
    print("")
    print("")
    return total

def roll_and_evaluate(how_many_dice, how_many_groups, k):
    grps_rolled = 0
    k_count = 0
    while grps_rolled < how_many_groups:
        if roll_group(how_many_dice) == k:
          k_count += 1
        grps_rolled += 1
    return k_count    
    

count_k = roll_and_evaluate(how_many_dice, how_many_groups, k)


print("If k is %d, and I roll %d dice %d times, the dice are equal to k %d of those times." % (k, how_many_dice, how_many_groups, count_k))

"""
#2a. Write a simulation that calculates the number of infections after 100 time periods, when you start with 1 infected person, with each time step, for each infected person, a 15% chance of being cured, and a 25% chance of infecting one new person.

import random

initial_infected = 1
time_to_run = 100

def infected_person():
    randomizer = 0
    randomizer = random.randint(1,100)
    if randomizer in range(1,15):
        print("cured")
        return "cured"
    elif randomizer in range(76,100):
        print("spreads")
        return "spreads" 
    else: 
        print("nothing happens...")
        return
   
def time_period(infected):
        tested = 0
        while tested < infected:
            condition = infected_person()
            if condition == "cured":
                infected += -1
            elif condition == "spreads":
                infected += 1
            print ("Infected: ", infected)
            tested += 1
        return infected
        
def over_time(infected, time):
     time_past = 0
     while time_past < time:
          infected = time_period(infected)
          time_past += 1

over_time(initial_infected, time_to_run)


#2b. Write a function that takes parameters N_start, N_times, P_infection and P_cure, representing the number of infected persons at the start, the number of time steps, the chance of infecting another person in each time step, and the chance of being cured in each time step, and that returns the number of infected persons at the end of the simulation.
#2c. Run the above simulation 20 times, with each time N_start=2, N_times=100, P_infection=0.25, P_cure=0.10. Experiment with different values to see results.
"""
import random

initial_infected = 3
time_to_run = 100
chance_of_cure = 15
chance_of_spread = 26

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

new_infected = iterate_time(initial_infected, time_to_run, chance_of_cure, chance_of_spread)

print("If we start with {} infected people and each hour each person has a {} percent chance of being cured and a {} percent chance of spreading the disease, after {} hours there will be {} infected people." .format(initial_infected, chance_of_cure, chance_of_spread, time_to_run, new_infected))



"""
#3a. Write a function that randomly, with equal probability for each outcome, returns either "up", "down", "left", or "right".
import random
import math
start_x = 0
start_y = 0
steps = 5
vector = 0, 0

def direction():
    #return x, y
    random_number = 0
    random_number = random.randint(1,100)
    if random_number in range(1,25):
        return 1, 0 #right
    elif random_number in range(26,50):
        return -1, 0 #left
    elif random_number in range(51,75):
        return 0, 1 #up
    else:
        return 0, -1 #down


def move(x, y):
    move = direction()
    print(move)
    x = x + move[0]
    y = y + move[1]
    return x, y


def iterate(steps, x, y):
    steps_completed = 0
    location = 0, 0
    while steps_completed < steps:
        movement = 0, 0
        movement = move(x, y)
        location = (location[0] + movement[0], location[1] + movement[1])
        steps_completed += 1
    return(location[0], location[1])


def measure(start_x, start_y, x, y):
    x_distance = 0
    y_distance = 0
    pythagorean = 0
    euclidean = 0
    x_distance = x - start_x
    y_distance = y - start_y
    pythagorean = (x_distance**2)+(y_distance**2)
    euclidean = math.sqrt(pythagorean)
    return euclidean


vector = iterate(steps, start_x, start_y)
print(measure(start_x, start_y, vector[0], vector[1]))









#3b. Write a function that takes a parameter N and then starting with (x,y) coordinates at (0,0), takes N steps in random directions, and returns the Euclidean distance between the start and end points.

#4a. Write a function that takes the borrowed amount, the interest rate, and the number of months as input parameters, that prints for each month the total borrowed amount and returns the end loan.
#4b. Change the above function by adding a parameter for the monthly downpayment and take this into account. For each month, the downpayment is subtracted after interest has been added (i.e. at the end of the month).