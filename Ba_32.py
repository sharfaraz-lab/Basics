#Write a program to print the sum of the first K natural numbers.
#Input Size : n <= 100000
#Sample Testcase :
#INPUT
#3
#OUTPUT
#6




x=int(input())
sum = 0
for i in range (0,x+1):
	sum = sum + i
print(sum)
