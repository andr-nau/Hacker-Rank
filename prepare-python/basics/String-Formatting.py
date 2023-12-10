"""
Problem: https://www.hackerrank.com/challenges/python-string-formatting/

Given an integer, , print the following values for each integer i from 1 to n:

    1. Decimal
    2. Octal
    3. Hexadecimal (capitalized)
    4. Binary

Prints
The four values must be printed on a single line in the order specified above for each i from 1 to 'number'.
Each value should be space-padded to match the width of the binary value of 'number' and the values should be separated by a single space.
"""

def print_formatted(number):
    #Set max width of all columns from width of HEX representation of the max number
    spacing = len('{:b}'.format(number))
    
    for num in range(number):
        for base in 'doXb': #Loop over the base for format: d - decimal, o - actal, X - hexadecimal, b - binary
            print('{0:{width}{base}}'.format(num+1, width=spacing, base=base), end=' ')
        print()

print_formatted(17) # HR test case