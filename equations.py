import sys
from utilities import comp_abs, comp_sqrt

def print_the_bajskorv(nm, flags):
    s = str(round(nm, 6))
    if s[-2 : ] == ".0":
        s = s[:-2]
    result = s
    if flags['c'] and not flags['b']:
        result = '\x1b[6;30;42m' + s + '\x1b[0m'
    return result + '\n'

def solve_linear_eq(data, flags):
    root = 0

    result = ""

    # ax + b = 0
    # b = data[0]; a = data[1]
    if (data[1] != 0.0):
        root = - (data[0] / data[1])
        result += "The solution is:\n"
        result += print_the_bajskorv(root, flags)
    elif (data[1] == 0.0 and data[0] != 0.0):
        result += "Linear equation: I don't have any roots in this case!\n"
    elif (data[0] == 0.0 and data[1] == 0.0):
        result += "Linear equation: I have infinitely many roots. In this case, any number is the root of the linear equation.\n"
    return result

def solve_quadratic_eq(data, flags):
    d = 0
    root_1 = 0
    root_2 = 0

    result = ""

    # calculate discriminant D = b2 - 4ac
    d = (data[1] * data[1]) - (4 * data[2] * data[0])
    if flags['c'] and not flags['b']:
        result += ('\x1b[6;33;45m' + "D = " + str(d) + '\x1b[0m' + '\n')
    else:
        result += "D = " + str(d) + '\n'
    # print("D = "+ str(d))

    if (d > 0):
        result += "Discriminant is strictly positive, the two solutions are:\n"
        # x1 = ((-b + sqrt(D)) / (2a))
        if flags['i']:
            result += ("(" + str(-data[1]) + " + " + str(comp_sqrt(d)) + ")" + " / " + "(" + "2" + " * " + str(data[0]) + ")\n")
        root_1 = ((-data[1] - comp_sqrt(d)) / (2 * data[2]))
        result += print_the_bajskorv(root_1, flags)
        # x2 = ((-b - sqrt(D)) / (2a))
        root_2 = ((-data[1] + comp_sqrt(d)) / (2 * data[2]))
        result += print_the_bajskorv(root_2, flags)
    elif (d == 0):
        result += ('\x1b[6;30;42m' + "Discriminant is equal to zero, the solution is:" + '\x1b[0m' + '\n')
        # print("Discriminant is equal to zero, the solution is:")
        # x1 = x2
        root_1 = ((-data[1] - comp_sqrt(d)) / (2 * data[2]))
        result += print_the_bajskorv(root_1, flags)
    elif (d < 0):
        result += ('\x1b[6;30;42m' + "Discriminant is less than zero, the equation has no real roots." + '\x1b[0m' + '\n')
        result += ("Discriminant is less than zero, the equation has no real roots.\n")

    return result
