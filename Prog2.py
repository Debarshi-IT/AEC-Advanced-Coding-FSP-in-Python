# Series Problem-2
# position   1   2   3   4   5    6    7
# total  = - 2 + 4 - 6 + 8 - 10 + 12 - 14 - ... n terms
n = int(input("Please enter the number of terms:"))
total = 0
for i in range(1, n + 1):
    term = ((-1)**(i))*(2*i)
    total = total + term
    print(f"For i = {i}, term = {term} and total = {total}...")
print(f"So the total of first {n} terms of th series is {total}...")
print("End of the program...")