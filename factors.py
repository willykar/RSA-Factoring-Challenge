#/usr/bin/env python3
import sys


def primef(m):
    if m <= 3:
        return int(m)
    if m % 2 == 0:
        return 2
    elif m % 3 == 0:
        return 3
    else:
        for a in range(5, int((m)**0.5) + 1, 6):
            if m % a == 0:
                return int(a)
            if m % (a + 2) == 0:
                return primef(m/(a+2))
    return int(m)


print(primef(int(sys.argv[1])))
