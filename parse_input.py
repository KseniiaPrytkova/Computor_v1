#!/usr/bin/env python

import re
import sys

def print_reduced_form(m):
    signs = []
    s = ""

    for i, e in enumerate(m[0]):
        if (e > 0):
            signs += [" + "]
        else:
            signs += [" - "]

    s = "Reduced form: " + str(m[0][0]) + " * X^" + str(0)
    if (len(m[0]) >= 2):
        s += signs[1] + str(m[0][1]) + " * X^" + str(1)
    if (len(m[0]) >= 3):
        s += signs[2] + str(m[0][2]) + " * X^" + str(2)
    s += " = 0"
    s = s.replace("+ -", "-")
    # print('\x1b[6;33;45m' + s + '\x1b[0m')
    print(s)

def check_parsed_input(s, r_1, r_2):
    s_2 = "".join([e[0] for e in r_1]) + "=" + "".join([e[0] for e in r_2])
    if s_2 != s:
        sys.stderr.write("usage: all terms must be of the form a * x^p\n" +
        "example: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\n")
        sys.exit(1)

def parse_input(s):
    # delete all spaces in a string:
    s = s.replace(" ", "")
    # ['5*X^0+4*X^1-9.3*X^2', '1*X^0']
    s_l = s.split('=')
    if len(s_l) != 2:
        sys.stderr.write("ERROR: exactly one equal sign expected\n")
        sys.exit(1)

    regexp = r"(([+-]?\d+(\.\d+)?)[*][Xx]\^([+-]?\d+(\.\d+)?))"
    r_1, r_2 = re.findall(regexp, s_l[0]), re.findall(regexp, s_l[1])

    check_parsed_input(s, r_1, r_2)

    m = [{0: [], 1: [], 2: []}, {0: [], 1: [], 2: []}]
    for res in r_1:
        m[0][int(res[3])] += [float(res[1])]
    for res in r_2:
        m[1][int(res[3])] += [float(res[1])]

    # FIXME: play sound.
    # FIXME: add flag -b: output to browser
    # FIXME: argparse: add flag -i

    n = [{}, {}]

    # Simplify: left.
    for key in m[0]:
        n[0][key] = sum(m[0][key])

    # Simplify: right.
    for key in m[1]:
        n[1][key] = sum(m[1][key])

    # Simplify: move all elements in the right to the left.
    for key in n[1]:
        if key in n[0]:
            n[0][key] = n[0][key] - n[1][key]
        else:
            n[0][key] = -n[1][key]

    print_reduced_form(n)

    # Get all x^y values from y=0 to y=2.
    res = [ n[0][i] if i in n[0] else "-" for i in range(len(n[0])) ]

    return(res)
