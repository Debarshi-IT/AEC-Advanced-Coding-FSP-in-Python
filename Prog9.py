                  
"""              
# Pattern Problem-2
n = 11 (User given ODD integer number)    m = (n + 1) // 2 = 6
                   i  .1  .2
                  -----------
.....*             1   5   x        (i, m, n)
....*.*            2   4   1  .1 => (m - i)
...*...*           3   3   3
..*.....*          4   2   5  .2 => (2 * i - 3)
.*.......*         5   1   7
*.........*       _6___0___9_ 
.*.......*         7   1   7
..*.....*          8   2   5  .1 => (i - m)
...*...*           9   3   3
....*.*           10   4   1  .2 => (2 * (n - i) - 1)
.....*            11   5   x
                  -----------
Generate this pattern using a single loop construct for any odd value for n. 
             
"""
n = 11
m = (n + 1) // 2  # 6
i = 1

while i <= n:
    if i <= m:
        spaces = m - i
        if i == 1:
            print(" " * spaces + "*")
        else:
            inner_dots = 2 * (i - 1) - 1
            print(" " * spaces + "*" + " " * inner_dots + "*")
    else:
        spaces = i - m
        if i == n:
            print(" " * spaces + "*")
        else:
            inner_dots = 2 * (n - i) - 1
            print(" " * spaces + "*" + " " * inner_dots + "*")
    i += 1

