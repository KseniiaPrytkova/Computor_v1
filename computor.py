#!/usr/bin/env python

import sys
import re
from parse_input import parse_input
from equations import solve_linear_eq, solve_quadratic_eq
import os
import random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import tempfile
import webbrowser

def play_sound():
    try:
        random.seed()
        sounds = [os.path.join("sounds/", file) for file in os.listdir("sounds") if file.endswith(".wav") or file.endswith(".WAV")]
        sound = random.choice(sounds)
        # print("sound: " + sound)
        pygame.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        time.sleep(2)
    except:
        pass

def open_in_browser(s):
    with tempfile.NamedTemporaryFile(prefix="index_", suffix=".html") as temp:
        temp.write(b'<HEAD>')
        temp.write(b'</HEAD>')
        temp.write(b'<BODY>')
        temp.write(s.encode('utf-8'))
        temp.write(b'</BODY>')
        temp.flush()
        webbrowser.open_new("file://" + temp.name)
        # os.system("open -a /Applications/Safari.app " + temp.name)
        # Needed since the tempfile will be deleted before the browser can access it otherwise.
        time.sleep(0.2)

def calc(data, flag):
    degree = 0
    i = 0

    while (i < len(data)):
        if (data[i] != 0.0):
            degree = i
        i += 1
    result = ""

    print("Polynomial degree: " + str(degree))
    if (degree >= 3):
        if flags['c'] and not flags['b']:
            result = ('\x1b[6;30;42m' + "The polynomial degree is stricly greater than 2, I can't solve." + '\x1b[0m' + '\n')
        else:
            result = ("The polynomial degree is stricly greater than 2, I can't solve.\n")
        sys.exit(1)
    elif (degree == 1 or degree == 0):
        # ax + b = 0
        if (degree == 0):
            if flags['c'] and not flags['b']:
                result = ('\x1b[6;30;42m' + "This equation has no solutions." + '\x1b[0m' + '\n')
            else:
                result = ("This equation has no solutions.\n")
            sys.exit(0)
        result = solve_linear_eq(data, flags)
    elif (degree == 2):
        # ax^2 + bx + c = 0
        result = solve_quadratic_eq(data, flags)
    else:
        if flags['c'] and not flags['b']:
            result = ('\x1b[6;30;42m' + "Error! Calculated degree is incorrect." + '\x1b[0m' + '\n')
        else:
           result = ("Error! Calculated degree is incorrect.\n") 

    if flags['b']:
        open_in_browser(result)
    else:
        sys.stdout.write(result)

    if flags['s']:
       play_sound()
    play_sound()

def get_args():
    data = []
    flags = {'c': False, 'i': False, 'b': False, 's': False}

    s = None
    for i in range(1, len(sys.argv)):
        arg = sys.argv[i].strip()
        if arg in ['-b', '-c', '-i', '-s']:
            flags[arg.replace('-', '')] = True
        elif not s:
            s = arg
        else:
            raise
    if not s:
        raise

    data = parse_input(s)

    return data, flags

if __name__ == "__main__":
    data = []
    flags = {}

    try:
        data, flags = get_args()
    except Exception as e:
        sys.stderr.write("usage: all terms must be of the form a * x^p\n" +
        "example: 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\n" + "flags avaliable:" + '\x1b[6;33;45m' + "-c, -i, -b, -s" + '\x1b[0m' + "\n")
        sys.exit(1)

    calc(data, flags)
