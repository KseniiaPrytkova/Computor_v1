import sys
import re
import subprocess

import sympy
from sympy import symbols,solve,sympify,evalf

from parse_input import parse_input

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: all terms must be of the form a * x^p\n" +
        "example: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
        sys.exit(1)

    s_eq = sys.argv[1].replace(" ", "").replace("X", "x")
    cmd = "python3 ./computor.py " + s_eq
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if err:
        sys.stderr.write("ERROR from program:\n" + err.decode('utf-8'))
        sys.exit(1)
    #print("Output:\n" + out.decode('utf-8'))

    eq = sympify("Eq(" + s_eq.replace("=", ",") + ")")
    sol = solve(eq, dict=True, rational=False)
    sol = [[e[a].evalf() for a in e] for e in sol]

    print("PROGRAM:\n" + out.decode('utf-8'))
    print("SYMPY:\n" + str(sol))












