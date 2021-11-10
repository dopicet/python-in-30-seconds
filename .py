# printing Hello world
print("Hello world")

# function
def func():
    print("Hello world")
func()

# list, tuple, set, dict
lst = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}
dct = {"a":1, "b":2}
# printing type
print(type(lst))
print(type(tuple))
print(type(set))
print(type(dct))

# class
class ABC:
    # constructor
    def __init__(self, n) -> None:
        self.n = n

    def func(self):
        print(self.n)

abc = ABC("Hello world")
abc.func()

# inheritance
from inspect import getmro

class Father:
    pass
class Son(Father):  # class son inherit from class Father
    pass

print(getmro(Son))

# simple game
import random
n = random.randint(1,5)
while True:
    usr = int(input("Enter Your Number: "))
    if usr == n:
        print("You won")
        break
    else:
        print("Not a correct number")
