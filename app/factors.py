# this file contains all of the rating factors in data structures.

# base premium amount
basePremium = 350

# dictionary associating dwelling coverage amounts with rating factors.
DwellingCoverage = { 
        100000 : 0.971,
        150000 : 1.104,
        200000 : 1.314,
        250000 : 1.471,
        300000 : 1.579,
        350000 : 1.761 
    }

# list of tuples associating the minumum home age (in each age range) with rating factors.
HomeAge = [
        (100 , 1.95), 
        (36 , 1.80), 
        (11 , 1.5), 
        (0 , 1.0)
    ]

# dictionary associating the roof types with rating factors. 
RoofType = { 
        "Asphalt Shingles" : 1.0,
        "Tin" : 1.7,
        "Wood" : 2.0
    }

# dictionary associating the number of units with a rating factor.
NumberOfUnits = { 
        1 : 1, 
        2 : .80, 
        3 : .80, 
        4 : .80 
    }