#!/usr/bin/env python

import sys
import re
from parse_input import parse_input


if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    # for i, arg in enumerate(sys.argv):
    #     print(f"Argument {i:>6}: {arg}")
    if (len(sys.argv) == 2):
        s = sys.argv[1]
        parse_input(s)
    else:
    	print("usage: all terms must be of the form a * x^p\n" +
        "example: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
