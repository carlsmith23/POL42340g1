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