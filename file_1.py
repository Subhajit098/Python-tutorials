# Python module to execute
import random
rad=random.randint(1,4)
print(rad)
print("hh")
from file_2 import *

print("File one __name__ is set to: {}" .format(__name__))


def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")