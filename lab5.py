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

while run = 1:
    print("Set (s)ize of the map")
    print("Set number of (a)gents")
    print("(G)enerate map")
    print("(P)rint map")
    print("(Q)uit")
    buffer = input("Select an option: ")
    if buffer == "q" or "Q":
        run = 0


#1c. Implement the map size functionality. If the user presses s or S, ask for the size of the map. Write a separate function for this.
#1d. Implement the agent number functionality. Write a separate function for this.

#2a. Expand the function written in 1c to not accept anything other than a number, and only a number between 1 and 100.
#2b. Expand the function written in 1d to only work when the size of the map is set and to not accept anything other than a number, and only a number between 1 and the number of cells. Since it is a square map, the number of cells is N * N, N being the length of one side of the square, as entered in 1e.

#3a. Update the function written in 1a, so that after the user sets the map size (2a), a map is automatically generated (use 2a from Lab 4).
#3b. Update the function written in 1a, so that after the user sets the number of agents (2b), the map is updated so that all agents are added (use 4 from Lab 4).

#4. Write a function to print the map, where zeroes are represented by "-" and ones by "X".