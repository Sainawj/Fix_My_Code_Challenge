#!/usr/bin/python3
""" FizzBuzz
    Change of logic if (i % 3) == 0 and (i % 5) == 0:
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    output = ""
    for i in range(1, n + 1):
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not (i % 3 == 0 or i % 5 == 0):
            output += str(i)
        output += " "
    print(output.strip())


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
