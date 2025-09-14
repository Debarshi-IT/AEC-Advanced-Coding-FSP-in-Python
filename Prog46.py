# find the number of set bits in a number n
# for n = 63 = 0011 1111, output will be 6
# for n = 41 = 32 + 8 + 1 = 0010 1001, output will be 3
def countSetBitsFast(n):     #  ans    n
    ans = 0                  # ----------
    while(n):                #  0      41 = 101001
        n = n & (n - 1)      #  1      41 & 40 = 101001 & 101000 = 101000 = 40
        ans = ans + 1        #  2      40 & 39 = 101000 & 100111 = 100000 = 32
        print("Looping")     #  3      32 & 31 = 100000 & 011111 = 0
    return ans
n = 41  # 63
print(f"For n = {n}, number of set bits = {countSetBitsFast(n)}")