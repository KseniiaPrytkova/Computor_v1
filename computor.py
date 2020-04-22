#!/usr/bin/env python

import sys
import re
from parse_input import parse_input

def ntsqrt(n):
    sgn = 0
    if n < 0:
        sgn = -1
        n = -n
    val = n
    while True:
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    if sgn < 0:
        return complex(0, val)
    return val

def calc(data):
    degree = 0
    d = 0
    root_1 = 0
    root_2 = 0

    print (data)
    degree = len(data) - 1
    if (degree >= 3):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        sys.exit(1)
    print("Polynomial degree: " + str(degree))

    # calculate discriminant D = b2 - 4ac
    d = (data[1] * data[1]) - (4 * data[0] * data[2])
    print("D = "+ str(d))

    if (d > 0):
        print("Discriminant is strictly positive, the two solutions are:")
        # x1 = ((-b + sqrt(D)) / (2a))
        root_1 = ((-data[1] + ntsqrt(d)) / (2 * data[0]))
        print (root_1)
        # x2 = ((-b - sqrt(D)) / (2a))
        root_2 = ((-data[1] - ntsqrt(d)) / (2 * data[0]))
        print (root_2)






if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    data = []
    if (len(sys.argv) == 2):
        s = sys.argv[1]
        data = parse_input(s)
        calc(data)
    else:
        print("usage: all terms must be of the form a * x^p\n" +
        "example: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
