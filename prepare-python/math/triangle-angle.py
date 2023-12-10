"""
Problem: https://www.hackerrank.com/challenges/find-angle/problem


"""


import sys
import math

a, b = [float(s) for s in sys.stdin]

c = math.sqrt(a**2 + b**2)
h = 1/2*math.sqrt(2*a**2 + 2*b**2 - c**2) #Apollonius's theorem in geometry

angle_MBC_rad = math.acos((h**2 + b**2 - (c/2)**2)/(2*h*b))
angle_MBC_deg = str(int(round(math.degrees(angle_MBC_rad), 0)))

print(angle_MBC_deg+u'\N{DEGREE SIGN}', file=sys.stdout)