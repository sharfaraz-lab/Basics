Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3




x=input()
y=input()
count=0
a=x.split()
N,K=int (a[0]),int (a[1])
b=y.split()
for i in range(0,N):
	if K==int(b[i]):
		count = count+1
	else:
		count = count
if count>=1:
	print("yes")
else:
	print("no")
