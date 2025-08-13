'''
Given an integer N, check if its second last digit is 7 or not. If the second last digit is 7, print 1, else print 0.
Note: The second last digit of an integer refers to the digit at the tens place, i.e. second digit from the right.

###Input
The first and only line of the input shall contain a single integer N.
###Output: If the second last digit of 
N is 7, print 1, else print 0, in a separate line.
'''
N=int(input("Enter a number: "))
a=(N//10)%10
if(a==7):
    print(1)
else:
    print(0)