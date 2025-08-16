a=int(input("Enter a number: "))
b=str(a)
if(b[0]=='-'):
    print("Invalid Input")
elif(b[::-1]==b):
    print("palindrome")
else:
    print("Not Palindrome")