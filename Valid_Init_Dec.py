import re
import os
import time

d = ["word", "numb"]


def low(s):
    if s == 'numb' or s == 'word':
        return False
    else:
        w = s.lower()
        return w


def st(s):
    pattern = r'^(numb|word)\s+([a-zA-Z_][a-zA-Z0-9_]*\s*(,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)\s*(=\s*[-+]?[0-9]*\.?[0-9]+|=\s*[\'"]?[a-zA-Z_][a-zA-Z0-9_]*[\'"]?)?(\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*\s*(=\s*[-+]?[0-9]*\.?[0-9]+|=\s*[\'"]?[a-zA-Z_][a-zA-Z0-9_]*[\'"]?)?)*$'

    return re.match(pattern, s) is not None


def v(inp):
    rw = (st(inp))

    p = r'\bnumb word|numb numb|word word|word numb\b'
    m = re.search(p, inp)

    if rw and not m:
        for a in inp:
            if low(a) and a in d:
                print("invalid")
                return

        print("Valid Declaration")
        return

    else:

        # only variable initialization
        pat2 = r'^[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(-?\d+(\.\d+)?|\'[^\']*\'|\"[^\"]*\")(\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(-?\d+(\.\d+)?|\'[^\']*\'|\"[^\"]*\"))*$'

        q = re.match(pat2, inp)
        if q:
            print("valid declaration")
            return

    print("invalid declaration ")


def time_delay():
    time.sleep(5)
    # clear the screen
    if os.name == 'nt':         # for windows
        os.system('cls')
    else:                       # for mac and linux
        os.system('clear')


def main():
    while (1):
        time_delay()
        print("1. Press 1 to check Variable Declaration and Intialization")
        print("2. Press 2 to exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            inp = input("Enter Your Statement: ")
            v(inp)
        elif choice == 2:
            break
        else:
            print("invalid choice")


main()
