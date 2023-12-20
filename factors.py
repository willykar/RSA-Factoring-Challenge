#!/usr/bin/python3
import sys

def factorize_number(n):
    factors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()
        for number in numbers:
            number = int(number)
            factor_pairs = factorize_number(number)
            for pair in factor_pairs:
                print(f"{number}={pair[0]}*{pair[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file>")
    else:
        file_path = sys.argv[1]
        factorize_file(file_path)
