def power_of_two(n):
    if (n > 0 and n & (n - 1) == 0): return True
    else: return False
n = 16
print(f"n = {n} and output = {power_of_two(n)}")
n = 64
print(f"n = {n} and output = {power_of_two(n)}")
n = 60
print(f"n = {n} and output = {power_of_two(n)}")