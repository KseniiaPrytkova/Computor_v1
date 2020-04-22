#!/usr/bin/env python

import re
import sys

# def gen_reduced_form():

def parse_input(s):
    # delete all spaces in a string:
    # 5*X^0+4*X^1-9.3*X^2=1*X^0
    s = s.replace(" ", "")
    # ['5*X^0+4*X^1-9.3*X^2', '1*X^0']
    s = s.split('=')
    # print (s)
    if len(s) != 2:
        print("ERROR: only one equal sign expected")
        sys.exit(1)

    regexp = r"(([+-]?\d+(\.\d+)?)[*][Xx]\^([+-]?\d+(\.\d+)?))"
    r_1, r_2 = re.findall(regexp, s[0]), re.findall(regexp, s[1])
    # print("r_1 = ", r_1)
    # print("r_2 = ", r_2)
    m = [{}, {}]
    for res in r_1:
        m[0][int(res[3])] = float(res[1])
    for res in r_2:
        m[1][int(res[3])] = float(res[1])

    for key in m[1]:
        if key in m[0]:
            m[0][key] = m[0][key] - m[1][key]
        else:
            m[0][key] = -m[1][key]

    # print("final: " + str(m[0]))
    # print("Reduced form: " + str(m[0][0]) + " * X^0" +
    #         str(m[0][1]) + " * X^1" +
    #         str(m[0][2]) + " * X^2")
    print("Reduced form:")
    for i in m[0]:
        print(str(m[0][i]) + " * X^" + str(i))
    print(" = 0")

    # Get all x^y values from y=0 to y=2.
    res = [ m[0][i] if i in m[0] else 0.0 for i in range(3) ]

    return(res)
