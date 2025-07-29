"""
# Pattern Problem-3
n = 11 (User given ODD integer number)    m = (n + 1) // 2 = 6
                   i   .   *
                  -----------
AAAAAAAAAAA        1   5   1       (i, m, n)
.BBBBBBBBB         2   4   3  . => (m - i)
..CCCCCCC          3   3   5
...DDDDD           4   2   7  * => (2 * i - 1)
....EEE            5   1   9
.....F            _6___0__11_ 
....GGG            7   1   9
...HHHHH           8   2   7  . => (i - m)
..IIIIIII          9   3   5
.JJJJJJJJJ        10   4   3  * => (2 * (n - i) + 1)
KKKKKKKKKKK       11   5   1

"""
while(True):
    n = int(input("Please enter the ODD integer for layer count: "))
    if (n % 2 == 1): break
m = (n + 1) // 2
for i in range(1, n + 1):
    if (i <= m): 
        b = (i - 1)
        ch = (2 * (m - i) + 1)
    else: 
        b = (n - i)
        ch = (2 * (i - m) + 1)
    print("." * b + chr(64 + i) * ch)