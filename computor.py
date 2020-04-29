#!/usr/bin/env python

import sys
import re
from parse_input import parse_input
# from utilities import comp_abs, comp_sqrt
from equations import solve_linear_eq, solve_quadratic_eq

def calc(data):
    degree = 0
    i = 0

    #print(data)
    #print ("len = " + str(len(data)))
    while (i < len(data)):
        if (data[i] != 0.0):
            degree = i
        i += 1

    #print('\x1b[6;33;45m' + "Polynomial degree: " + str(degree) + '\x1b[0m')
    # print("Polynomial degree: " + str(degree))
    # print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    if (degree >= 3):
        sys.stderr.write("The polynomial degree is stricly greater than 2, I can't solve.\n")
        sys.exit(1)
    # elif (degree == 0):
    #     print("degree == 0")
    elif (degree == 1 or degree == 0):
        # ax + b = 0
        if (degree == 0):
            print('\x1b[6;30;42m' + "This equation has no solutions." + '\x1b[0m')
            # print("This equation has no solutions.")
            sys.exit(0)
        #print("linear")
        solve_linear_eq(data)
    elif (degree == 2):
        # ax^2 + bx + c = 0
        solve_quadratic_eq(data)
    else:
        sys.stderr.write('\x1b[6;30;42m' + "Error! Calculated degree is incorrect." + '\x1b[0m\n')
        # print ("Error! Calculated degree is incorrect.")

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
        sys.stderr.write("usage: all terms must be of the form a * x^p\n" +
        "example: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\n")
