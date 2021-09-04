"""Counting letters in a string."""

__author__ = "730232764"


# Begin your solution here...
what_letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
position: int = 0 
counter: int = 0

while position < len(word):
    if word[position] == what_letter: 
        counter = counter + 1 
    position = position + 1 
print("Count:", counter) 