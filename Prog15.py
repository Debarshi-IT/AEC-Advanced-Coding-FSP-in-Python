'''
Class Assignment-2: Number Theory & Mathematical Problems
Krishnamurthy Number
📌 Problem Statement: A number is a Krishnamurthy number if the sum of the factorials of its digits equals the number itself.
✅ Example 1: 145 → (1! + 4! + 5!) = 145
✅ Example 2: 40585 → (4! + 0! + 5! + 8! + 5!) = 40585
'''
import math

def ik(num):
    original = num
    sum_of_factorials = 0
    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
    return sum_of_factorials == original
numbers_to_test = [1, 2, 145, 40585, 100, 123]
for number in numbers_to_test:
    if ik(number):
        print(f"{number} is a Krishnamurthy number ✅")
    else:
        print(f"{number} is NOT a Krishnamurthy number ❌")