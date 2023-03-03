def generate_list(N):
  L= []
  i = 0
  while i < (N *N):
    if i%2 == 0:
      L.append(0)
    else:
      L.append(1)
#    print(L)
    i += 1
  return L
#jos answers lab 2ba: Write a function that takes as parameters an x and y value, and a list length N, and returns a list index as follows: i = (x-1) * N + (y-1).

def get_index(x, y, N):
  return (x-1) * N + (y-1)
#print(get_index(1, 1, 5) == 0)
#print(get_index(1, 5, 5) == 4)
#print(get_index(3, 4, 5) == 13)

#jos answer 2bb: Write a function that takes a parameter L, which is a list of ones and zeroes, and parameters x and y representing coordinates, which returns the value of that point in the list using 2b. Note that N is the square root of the length of the list. Test using a list generated in 2a.

import math

def get_value(x, y, L,bools):
  N = int(math.sqrt(len(L)))
  range_1 = range(1,N+1)
  if x not in range_1: 
    return("error x")
  elif y not in range_1:
    return("error y")
  else:
    if bools == False:
      return L[get_index(x, y, N)]
    else:
      L[get_index(x,y,N)] = 1 - L[get_index(x,y,N)]
      return L[get_index(x,y,N)]

#print(get_value(2, 3, generate_list(5),True))

#2d Modify the function in 2d to take an additional boolean parameter, which if set, changes the value at the point in the list at (x,y). The default value of the parameter should be False, so that if you do not use it, it will by default not change the data.

#3a. Write a function that takes a list and returns random x and y coordinates. The x and y coordinates have to be valid, given the length of the list.

#import random
#test_list = generate_list(5)
#def randlist(L):
#  N = int(math.sqrt(len(L)))
#  return [random.randint(1,N),random.randint(1,N)]
#print(randlist(test_list))

#3b Write a modification of 3a, returning only coordinates for a cell that has a zero value.
import random
test_list = generate_list(5)
def randlist(L):
  N = int(math.sqrt(len(L)))
  coord = [random.randint(1,N),random.randint(1,N)]
  x = coord[0]
  print(x)
  y = coord[1]
  print(y)
  num = get_value(x,y,L,False)
  print(num)
  if num == 0:
    return coord
  else:
    print ("value at coordinates is not a zero")
print(randlist(test_list))
