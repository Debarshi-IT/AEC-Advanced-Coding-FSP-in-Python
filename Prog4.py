# Series Problem-4
# position   1   2   3   4   5    6   7   8   9   10   11  12
# total  =   1 + 2 + 3 + 4 + 10 + 5 + 6 + 7 + 8 + 26 + 9 + 10 + ... n terms
n = int(input("Please enter the number of terms:"))
total = 0
fsum = tsum = 0
term = 1
for i in range(1, n + 1):
    if (i % 5 == 0):
        fsum = fsum + tsum
        print(f"For i = {i}, adding tsum = {tsum}...")
        tsum = 0
    else:
        fsum = fsum + term
        tsum = tsum + term
        print(f"For i = {i}, adding term = {term}...")
        term = term + 1
print(f"So the total of first {n} terms of the series is {fsum}...")
print("End of the program...")