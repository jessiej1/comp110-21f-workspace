"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730232764"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint 

# Begin your solution here...

print("Your fortune cookie says...")

random_number = randint(0, 5) 

if random_number == 0:
    print("You have a secret admirer.")
else: 
    if random_number == 1: 
        print("A dream you have will come true.")
    else: 
        if random_number == 2: 
            print("You miss 100 percent of the shots you don't take.")
        else: 
            if random_number == 3: 
                print("Today is the day to try something new.")
            else: 
                if random_number == 4: 
                    print("You will have a pleasant surprise in the coming days.")
                else: 
                    if random_number == 5: 
                        print("A new academic venture is on the horizon.")

print("Now, go spread positive vibes!")