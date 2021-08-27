"""COMP110 Ex01 Numeric Operators Practice!"""

__author__ = "730232764" 

left_side: str = input("Left-hand side: ") 
right_side: str = input("Right-hand side: ")
print(left_side, "**", right_side, "is", int(left_side) ** int(right_side))
print(left_side, "/", right_side, "is", int(left_side) / int(right_side))
print(left_side, "//", right_side, "is", int(left_side) // int(right_side))
print(left_side, "%", right_side, "is", int(left_side) % int(right_side))