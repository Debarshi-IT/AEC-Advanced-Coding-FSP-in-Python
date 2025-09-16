'''
Given a non-empty array of integers, every element appears twice except one. Find that single one.
* Example-1: input: [11, 33, 22, 44, 33, 11, 22], output: 44
* Example-2: input: [10, 20, 40, 30, 20, 10, 60, 60, 30], output: 40
'''
def SingleNumberOne(numbers):
    number_count = {}
    for num in numbers:
        if num not in number_count:
            number_count[num] = 1
        else:
            number_count[num] += 1
    print(number_count)
    for num in numbers:
        if number_count[num] == 1: return num
print(SingleNumberOne([11, 33, 22, 44, 33, 11, 22]))
print(SingleNumberOne([10, 20, 40, 30, 20, 10, 60, 60, 30]))