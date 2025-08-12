'''
Odd Even Multiple
Given an integer N,

If N is not divisible by 3 then print −1,
If N is an odd multiple of 3 the print 1,
else if N is an even multiple of 3 then print 0.
'''
N=int(input("Enter a number: "))
a=N/3
if(N%3 != 0):
    print(-1)
elif(a%2 != 0):
    print(1)
else:
    print(0)