#Refactoring is the technical term for rewriting code that already works, to improve readability and maintainability of the code. For example, sometimes we might split a function into multiple, easier to read functions, that have very clear objectives.

#Since an object-oriented systems design is generally chosen because of its maintainability, an example of refactoring would be to turn a program written using a procedural paradigm into one that is more object-oriented. In Lab 6 we will take the set up of Lab 5 and make it object-oriented.

#1.   Refactor the code from Lab 4 using an object-oriented design, with separate files for each class, in the following steps:
#1a.  Create an Agent class, which for now is just an empty class.
#1b.  Create a Cell class, which can be either empty, or contains one agent. It should have a method isEmpty() that returns True when there is no agent and False otherwise. It should have a setAgent(agent) function to add an agent to the cell.
#1c.  Create a Map class, which consists of a list of cells. Refactor the functions from Lab 4, Question 2, to become methods in this class.
#1d.  Add the functions from Lab 4, Question 3, to the Map class.
#1e.  Create a Simulation class, with a run() function that prints the menu and asks for input. Implement all of Lab 5 in our new object-oriented setup.

#Especially 1e is not very specific and will require some thinking. Brainstorm in your group what the necessary class variables and class methods might be to make this all work.


from simulation import Simulation

simulation = Simulation()
run = 1

while run == 1:
    run = simulation.main_loop()