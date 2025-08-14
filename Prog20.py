'''
You're given two numbers  L and R. Print all odd numbers between L and R (both inclusive) in a single line separated by space, in ascending (increasing) order.

###Input:
First-line will contain two numbers L and R.
###Output: 
Print all odd numbers in a single line separated by space, in ascending (increasing) order.
'''
L=int(input("Enter starting number: "))
R=int(input("Enter ending number: "))
for i in range(L,R+1):
    if(i%2 != 0):
        print(i)