# replace i-th bit in n with b
def replaceBit(n, i, b):
    mask1 = ~(1 << i)  # clearing mask
    mask2 = b << i     # writing mask
    n = n & mask1
    n = n | mask2
    return n
n = 63
i = 4
b = 0
print(f"n = {n}, i = {i}, b = {0} and result = {replaceBit(n, i, b)}")