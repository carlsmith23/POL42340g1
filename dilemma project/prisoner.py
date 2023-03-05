import random


first_name = ["Archie", 
                "Billy",
                "Charlie",
                "Donnie",  
                "Eddie",
                "Frankie",
                "Gerry",
                "Harry",
                "Izzy",
                "Johnny",
                "Kenny",
                "Lenny",
                "Manny",
                "Normie",
                "Ozzie",
                "Patty",
                "Q",
                "Rusty",
                "Sammy",
                "Timmy",
                "U",
                "Vinnie",
                "Willy",
                "X",
                "Y",
                "Z", 
                ]

last_name = ["Angry Eyes",
                "Bonecrusher",
                "the Crime Doer",
                "Da Kid",
                "Eggbreath",
                "Fancypants",
                "Goofballs",
                "the Horse",
                "I",
                "J",
                "K",
                "L",
                "Moneybags",
                "N",
                "One Eye",
                "the Professor",
                "Q",
                "R",
                "S",
                "Tightlips",
                "the Usurper",
                "Vicious",
                "Wonderful",
                "X",
                "Y",
                "Zero"
                ]

i = 0
reps = 100
while i < reps:
    fname = random.randint(0,25)
    lname = random.randint(0,25)
    print(first_name[fname] + " " + last_name[lname])
    i += 1
  