"""COMP110 Ex01 Practice with Relational Operators."""

__author__ = "730232764"

left_hand: str = input("Left-hand side: ") 
right_hand: str = input("Right-hand side: ")
print(left_hand, "<", right_hand, "is", int(left_hand) < int(right_hand))
print(left_hand, ">=", right_hand, "is", int(left_hand) >= int(right_hand))
print(left_hand, "==", right_hand, "is", int(left_hand) == int(right_hand))
print(left_hand, "!=", right_hand, "is", int(left_hand) != int(right_hand))