# find the number of set bits in a number n
# for n = 63 = 0011 1111, output will be 6
# for n = 41 = 32 + 8 + 1 = 0010 1001, output will be 3
def countSetBits(n):
    ans = 0
    while(n):
        ans += (n & 1)
        n = n >> 1
        print("Looping")
    return ans
n = 41  # 63
print(f"For n = {n}, number of set bits = {countSetBits(n)}")