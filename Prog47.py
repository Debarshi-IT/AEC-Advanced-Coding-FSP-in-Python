'''
Problem on "Power of Two"
Given an integer number n, write a function to determine if it is a power of two or not.

Example: * if n = 16, output = True * if n = 64, output = True * if n = 60, output = False
'''
def power_of_two(n):
    power = 0
    while (2 ** power < n):
        power += 1
    if (2 ** power == n): return True
    else: return False
n = 16
print(f"n = {n} and output = {power_of_two(n)}")
n = 64
print(f"n = {n} and output = {power_of_two(n)}")
n = 60
print(f"n = {n} and output = {power_of_two(n)}")