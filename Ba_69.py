#Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
#Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
#Sample Testcase :
#INPUT
#2 5
#OUTPUT
#3

x=input()
a=list(map(int,x.strip().split()))
x=max(a)
y=min(a)
count=0
for j in range(y,x+ 1):  
   if j > 1:  
       for i in range(2,j):  
           if (j % i) == 0:  
               break  
       else:  
           count=count+1
print(count)
