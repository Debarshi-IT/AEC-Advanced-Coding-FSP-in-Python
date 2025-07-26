# Pattern Problem-1
"""
n = 11 (User given ODD integer number)

.....*
....***
...*****
..*******
.*********
***********
.*********
..*******
...*****
....***
.....*

"""
n = 11
mid = n / 2
i = 0

while i < n:
    if i <= mid:
        stars = 2 * i + 1
    else:
        stars = 2 * (n - i - 1) + 1
    spaces = (n - stars) // 2
    print(" " * spaces + "*" * stars)
    i += 1
 
