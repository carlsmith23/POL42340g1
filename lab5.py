#1a. Write a function that creates a loop with a set of menu options. Whatever the user presses, it should print the menu again.


#def get_input_number():
#  input_continue = True
#  while input_continue:
#    print("""please select your choice:
#    a.
#    b.
#    c.
#    d.
#    """)
#    input_choice = input()
#  return input_choice
#get_input_number()
#2a. Expand the function written in 1c to not accept anything other than a number, and only a number between 1 and 100.

def set_map_size():
  range_1 = range(1,100)
  map_size = input("please enter a numeric value for size: ")
  print(type(map_size))

  while map_size.isnumeric() == False:
    map_size = input("Please input a numeric value:  ")
    if map_size.isnumeric() == True:
      continue
      
  while map_size.isnumeric():
    if int(map_size) in range_1:
      return map_size
      map_size.isnumeric() == False
    elif int(map_size) not in range_1:
      map_size = input("Please input number between 1 and 100: ")
    else:
      print ("please enter a numeric value:  ")


def set_agent_num():
  agent_num = input("Please enter agent number:  ")
  while agent_num.isnumeric() == False:
    agent_num = input("please enter a numeric value for number: ")  
    
  return agent_num

  
#Implement the quit functionality: if the user presses q or Q, it should exit the menu loop (and thus the program).a
def get_input_number():
  input_continue = True
  while input_continue:
    print("""please select your choice:
    Set (s)ize of the map
    Set number of (a)gents
    (G)enerate map
    (P)rint map
    (Q)uit
    """)
    input_choice = input()
    if input_choice == "q" or input_choice == "Q":
      input_continue = False
    elif input_choice == "s" or input_choice == "S":
      set_map_size()
    elif input_choice == "a" or input_choice == "A":
      set_agent_num()
  return 
get_input_number()
