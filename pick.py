#! /usr/bin/python3

import random
import sys

probs_path = "https://raw.githubusercontent.com/jmccall/marchmadness/main/probs.txt"

def main(args):
    ''' Do stuff '''
    pick = random.randint(0, 69)
    print(pick)
    return 0


if __name__ == "__main__":
    main(sys.argv)
