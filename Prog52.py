'''
Given a non-empty array of integer numbers num, in which exactly two numbers appear only once.

And all the other numbers appear exactly twice. Find those two numbers that appear only once.

Example-1: input: [11, 33, 22, 44, 33, 11, 22, 55], output: [44, 55] or [55, 44]
Example-2: input: [10, 20, 40, 30, 20, 10, 60, 60, 30, 50], output: [40, 50] or [50, 40]
The algorithm should run in linear time complexity. Can we implement it with constant space complexity?
'''
def singleNumber2(nums):
    result = []
    for num in nums:
        if (nums.count(num) == 1): result.append(num)
    return result
print(singleNumber2([11, 33, 22, 44, 33, 11, 22, 55]))
print(singleNumber2([10, 20, 40, 30, 20, 10, 60, 60, 30, 50]))