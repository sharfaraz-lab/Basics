#Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
#Input Size N <= 100000
#Sample Testcase :
#INPUT
#4
#4 3 2 1
#OUTPUT
#0


x=int(input())
A=input()
a=list(map(int, A.strip().split()))
def AND(a, x) :  
    ans = a[0] 
    for i in range(x) : 
        ans &= a[i] 
          
    return ans 
print(AND(a, x)) 
