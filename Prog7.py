# Series Problem-5
# position   1   2   3   4   5   6   7
# total  =   4 + 7 + 4 + 7 + 4 + 7 + 4 + ... n terms
n = int(input("Please enter the number of terms: "))
term = 4     # initial term
total = 0
for i in range(1, n + 1):
    total = total + term
    print(f"For i = {i}, term = {term} and total = {total}...")
    term=(lambda term:{4:7,7:4}.get(term))(term)
    #term=term^3
    #term=4 if (total%11==0)else 7
    #term=int(5.5+((-1)**(i+1))*1.5)
    #term=5.5 +- 1.5
    #term=term+((-1)**(i+1))*3
    #term=28 //term
    #term=11-term
    #term=4 if(term==7) else 7 #ternary operation
    #if (term == 4): term = 7
    #else: term = 4
print(f"So the total of first {n} terms of the series is {total}...")
print("End of the program...")