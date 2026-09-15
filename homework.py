#Write the code to determine if a number is a perfect square or not.
import math
x = int(input("Enter a number: "))
if x == 0:
    print("LMAO DED U REALLY THOUGHT 0 WAS A PERFECT SQUARE 🤣")
elif x < 0:
    print("Negative numbers cannot be perfect squares")
else:
    y = int(x ** 0.5)
    if y * y == x:
        print("perfect square")
    else:
        print("not a perfect square")