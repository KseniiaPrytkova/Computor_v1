#!/usr/bin/env python

import sys
import re
from parse_input import parse_input
from utilities import comp_abs, comp_sqrt

def calc(data):
    degree = 0
    d = 0
    root_1 = 0
    root_2 = 0
    i = 0

    print(data)
    while (i < len(data)):
        if (data[i] != 0.0):
            degree += 1
        i += 1
    degree -= 1

    print("Polynomial degree: " + str(degree))

    if (degree > 3):
        print("The polynomial degree is stricly greater than 2, I can't solve.")
        sys.exit(1)
    elif (degree == 1):
        # ax + b = 0
        print("The solution is:")
        root_1 = - (data[0] / data[1])
        print("%.6f" % root_1)
    elif (degree == 2):
        # ax^2 + bx + c = 0
        # calculate discriminant D = b2 - 4ac
        d = (data[1] * data[1]) - (4 * data[2] * data[0])
        print("D = "+ str(d))

        if (d > 0):
            print("Discriminant is strictly positive, the two solutions are:")
            # x1 = ((-b + sqrt(D)) / (2a))
            # print ("(" + str(-data[1]) + " + " + str(comp_sqrt(d)) + ")" + " / " + "(" + "2" + " * " + str(data[0]) + ")")
            root_1 = ((-data[1] - comp_sqrt(d)) / (2 * data[2]))
            print("%.6f" % root_1)
            # x2 = ((-b - sqrt(D)) / (2a))
            root_2 = ((-data[1] + comp_sqrt(d)) / (2 * data[2]))
            print("%.6f" % root_2)






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
