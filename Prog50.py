def SingleNumberOne(numbers):
    result = 0
    for num in numbers:
        result = result ^ num
    return result
print(SingleNumberOne([11, 33, 22, 44, 33, 11, 22]))
print(SingleNumberOne([10, 20, 40, 30, 20, 10, 60, 60, 30]))