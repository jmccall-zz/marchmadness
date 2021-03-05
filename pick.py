#! /usr/bin/python3

import random
import sys

probs_path = "https://raw.githubusercontent.com/jmccall/marchmadness/main/probs.txt"

def main(argv):
    ''' Do stuff '''

    if len(argv) != 4:
        print('Usage: pick.py SEED_1 SEED_2 WIN_PROBABILITY')
        return 1

    SEED_1 = int(argv[1])
    SEED_2 = int(argv[2])
    WIN_PROB = int(argv[3])

    print('{} vs. {} | {} win percentage: {}'.format(SEED_1, SEED_2, SEED_1, WIN_PROB))


    for _ in range(69):
        pick = random.randint(0, 100)

    print(pick)
    if pick <= WIN_PROB:
        winner = SEED_1
    else:
        winner = SEED_2

    print('Winner: {}'.format(winner))
    return 0


if __name__ == "__main__":
    main(sys.argv)
