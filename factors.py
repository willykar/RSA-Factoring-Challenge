#!/usr/bin/python3
import sys


def factorize(num):
    fact = 2
    while (num % fact):
        if (fact <= num):
            fact += 1

    factor2 = num // fact
    return (factor2, fact)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

filename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()

for line in lines:
    num = int(line.rstrip())
    factor2, fact = factorize(num)
    print(f"{num} = {factor2} * {fact}")
