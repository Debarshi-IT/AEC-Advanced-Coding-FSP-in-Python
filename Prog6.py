# Series Problem-5
# position   1   2   3   4   5   6   7
# total  =   4 + 7 + 4 + 7 + 4 + 7 + 4 + ... n terms
n = int(input("Please enter the number of terms"))
term = 4     # initial term
total = 0
for i in range(1, n + 1):
    total = total + term
    print(f"For i = {i}, term = {term} and total = {total}...")
    if (term == 4): term = 7
    else: term = 4
print(f"So the total of first {n} terms of the series is {total}...")
print("End of the program...")