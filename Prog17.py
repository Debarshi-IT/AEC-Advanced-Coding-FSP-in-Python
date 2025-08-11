'''
Raju is planning to visit his favourite restaurant. He shall travel to it by bus. Only the buses whose numbers are divisible by 
5 or by 6 shall take him to his destination. You are given a bus number N. Find if Raju can take the bus or not.
Print YES if he can take the bus, otherwise print NO.
###Sample Input 1:
60
###Sample Output 1:
YES
###Sample Input 2:
16
###Sample Output 2:
NO
###Sample Input 3:
20
###Sample Output 3:
YES
'''
a=int(input("Enter a number: "))
if(a%5==0 and a%6==0):
    print("YES")
else:
    print("NO")