"""Repeating a beat in a loop."""

__author__ = "730232764"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ") 
counter: int = int(input("How many times do you want to repeat it? ")) 
result: str = beat

if counter <= 0: 
    print("No beat...")
else: 
    while counter > 1: 
        result = result + " " + str(beat) 
        counter = counter - 1 
        
    print(str(result))  
    