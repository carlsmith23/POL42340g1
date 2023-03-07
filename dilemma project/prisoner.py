import random

class prisoner
    def __init__(self, name, prisonerNumber, number_of_colors, color, crime, strategy, imprisoned, sentence):
        self.name = first_name[fname] + " " + last_name
        self.prisonerNumber = pnumber
        self.color = color[pcolor]
        self.strategy = strategy[pstrat]
        self.imprisoned = True
        self.sentence = sentence

def generate_name():
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
    fname = random.randint(0,25)
    lname = random.randint(0,25)
    name = first_name[fname] + " " + last_name[lname]
    return name

def set_prisoner_number():
    return pnumber    

def set_random_color(number_of_colors):
    colors = ["Red",
                "Blue,
                "Yellow",
                "Green",
                "Orange",
                "Purple"
                ]
    color = random.randint(0, number_of_colors)
    return colors[color]

def set_strategy():
    strategies = ["Altruist", 
                    "Egoist", "Ethnocentrist", "Cosmopolitan"
                    ]
        strategy = random.randint(0,3)
        return strategies[stategy]
        



