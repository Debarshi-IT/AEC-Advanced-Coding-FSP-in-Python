# complement the i-th bit of the number n
#                   7654 3210
# 25 = 16 + 8 + 1 = 0001 1001
#          1 << 2 = 0000 0100 ^
#                   ---------
#                   0001 1101 => 29
def complementBit(n, i):
    return n ^ (1 << i)
n = 25
p = 2
print(f"n = {n} and result = {complementBit(n, p)}")