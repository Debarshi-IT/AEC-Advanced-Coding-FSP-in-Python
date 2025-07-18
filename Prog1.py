# Series Problem-1
# position 1   2   3   4   5   6    7
# total  = 1 - 3 + 5 - 7 + 9 - 11 + 13 - ... n terms
n = int(input("Please enter the number of terms:"))
total = 0
for i in range(1, n + 1):
    term = ((-1)**(i+1))*(2*i-1)
    total = total + term
    print(f"For i = {i}, term = {term} and total = {total}...")
print(f"So the total of first {n} terms of th series is {total}...")