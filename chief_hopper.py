#!/usr/bin/env python3
from sys import stdin

N = int(stdin.readline().strip())
heights = [int(x) for x in stdin.readline().split()]

def checker(E):
    for h in heights:
        if E < 0:
            return False
        E = 2*E - h
    return E >= 0

min_energy_upper_bound = max(heights)
min_energy_lower_bound = 0

while min_energy_upper_bound > min_energy_lower_bound:
    to_try = (min_energy_upper_bound + min_energy_lower_bound)//2
    if checker(to_try):
        min_energy_upper_bound = to_try
    else:
        min_energy_lower_bound = to_try+1

print(min_energy_upper_bound)