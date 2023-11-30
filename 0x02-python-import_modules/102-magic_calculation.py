#!/usr/bin/python3
from magic_calculation_102 import add, sub

<<<<<<< HEAD

def magic_calculation(a, b):
=======
>>>>>>> f8a5f9e4c3c50b2dae67063341c0e4584c03b2c2
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return (sub(a, b))
