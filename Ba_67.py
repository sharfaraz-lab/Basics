Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat




X=input()
def split(X): 
    return [char for char in X] 
b=split(X)
Y=len(b)
for i in range(0,Y,2):
	temp = b[i]
	b[i] = b[i+1]
	b[i+1] = temp
for i in range (0,Y):
	print(b[i],end="")
