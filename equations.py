import sys
from utilities import comp_abs, comp_sqrt

def print_the_bajskorv(nm, flag):
    s = str(round(nm, 6))
    if s[-2 : ] == ".0":
        s = s[:-2]
    if (flag == "-c"):
        print('\x1b[6;30;42m' + s + '\x1b[0m')
    else:
        print(s)

def solve_linear_eq(data, flag):
    root = 0

    # ax + b = 0
    # b = data[0]; a = data[1]
    if (data[1] != 0.0):
        root = - (data[0] / data[1])
        print("The solution is:")
        print_the_bajskorv(root, flag)
    elif (data[1] == 0.0 and data[0] != 0.0):
        print ("Linear equation: I don't have any roots in this case!")
        sys.exit(0)
    elif (data[0] == 0.0 and data[1] == 0.0):
        print("Linear equation: I have infinitely many roots. In this case, any number is the root of the linear equation.")
        sys.exit(0)


def solve_quadratic_eq(data, flag):
    d = 0
    root_1 = 0
    root_2 = 0

    # calculate discriminant D = b2 - 4ac
    d = (data[1] * data[1]) - (4 * data[2] * data[0])
    if (flag == "-c"):
        print('\x1b[6;33;45m' + "D = " + str(d) + '\x1b[0m')
    else:
        print ("D = " + str(d))
    # print("D = "+ str(d))

    if (d > 0):
        print("Discriminant is strictly positive, the two solutions are:")
        # x1 = ((-b + sqrt(D)) / (2a))
        # print ("(" + str(-data[1]) + " + " + str(comp_sqrt(d)) + ")" + " / " + "(" + "2" + " * " + str(data[0]) + ")")
        root_1 = ((-data[1] - comp_sqrt(d)) / (2 * data[2]))
        print_the_bajskorv(root_1, flag)
        # x2 = ((-b - sqrt(D)) / (2a))
        root_2 = ((-data[1] + comp_sqrt(d)) / (2 * data[2]))
        print_the_bajskorv(root_2, flag)
    elif (d == 0):
        print('\x1b[6;30;42m' + "Discriminant is equal to zero, the solution is:" + '\x1b[0m')
        # print("Discriminant is equal to zero, the solution is:")
        # x1 = x2
        root_1 = ((-data[1] - comp_sqrt(d)) / (2 * data[2]))
        print_the_bajskorv(root_1, flag)
    elif (d < 0):
        print('\x1b[6;30;42m' + "Discriminant is less than zero, the equation has no real roots." + '\x1b[0m')
        print("Discriminant is less than zero, the equation has no real roots.")

