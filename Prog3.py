# Series Problem-3
# position   1    2    3    4    5     6     7
# total  =   2! + 4! + 6! + 8! + 10! + 12! + 14! + ... n terms
n = int(input("Please enter the number of terms:"))
total = 0
factorial = 2  # denoting first term as 2!
for i in range(1, n + 1):
    total = total + factorial
    print(f"For i = {i}, factorial = {factorial} and total = {total}...")
    factorial = factorial * (2*i+1) * (2*(i+1))
print(f"So the total of first {n} terms of the series is {total}...")
print("End of the program...")