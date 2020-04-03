#Given base(B) and height(H) of a triangle find its area.
#Input Size : N <= 1000000
#Sample Testcase :
#INPUT
#2 4
#OUTPUT
#4




a=input()
A=a.split()
b,h = int(A[0]),int(A[1])
area = 0.5*b*h
print(area)
