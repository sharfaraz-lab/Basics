Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.
Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes




a=input()
A=a.split()
x,y,z=int (A[0]),int (A[1]),int (A[2])
if x == y == z:
	print("no")
elif x==y or y==z or z==x:
	print("no")
else:
	print("yes")
