# find the i-th bit from the right in number n
def getBit(n, i):
    mask = 1 << i
    return 1 if (n & mask) else 0
#                   7654 3210
# 25 = 16 + 8 + 1 = 0001 1001
#          1 << 4 = 0001 0000 &
#                   ---------
#                   0001 0000 != 0 => 1
n = 25
p = 4
print(f"Bit at place {p} in {n} is {getBit(n, p)}")
p = 2
print(f"Bit at place {p} in {n} is {getBit(n, p)}")