# clear all bits in n from bit positions i (right) to j (left) bit positions
#                                7654 3210
# 63 = 32 + 16 + 8 + 4 + 2 + 1 = 0011 1111
# let i = 4 and j = 2               ----
# So result =                    0010 0011 => 32 + 2 + 1 = 35
def clearRangeItoJ(n, i, j):
    mask1 = (-1) << (i + j -1)
    mask2 = ~((-1) << j)
    mask3 = mask1 | mask2
    return n & mask3
n = 63
i = 4
j = 2
print(f"n = {n}, i = {i}, j = {j} and result = {clearRangeItoJ(n, i, j)}")