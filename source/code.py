import random

prompt = input("How many integers do you want to print?")
Lbound = input("What do you want the lower bound to be?")
Ubound = input("What do you want the upper bound to be?")

prompt = int(prompt)
Lbound = int(Lbound)
Ubound = int(Ubound)

n = 1

while n <= prompt:
    print(random.randint(Lbound, Ubound))
    n = n + 1
