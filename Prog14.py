'''
Class Assignment-1: Madam Number (Palindrome Number)
📌 Problem Statement: A number is a Madam number if it remains the same when reversed.
✅ Example 1: 121 → Reverse = 121 ✅
✅ Example 2: 1331 → Reverse = 1331 ✅
'''
a=int(input())
b=str(a)
if(b==b[::-1]):
    print("Madam number")
else:
    print("Not Madam number")