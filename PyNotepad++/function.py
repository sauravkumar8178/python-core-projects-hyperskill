def mes():
	print("Hello World")
	
mes()

print("Sum operation using return statement")
def sum_of_two_num(n1,n2):
	sum=n1+n2
	print("Sum=",sum)
	return sum                         #return statement using the return values in the function name like- s1 stored the value of (sum_of_two_num) &  ''' 
num1=int(input("Enter num1:"))         #(sum_of_two_num) stored the sum value using return statement.
num2=int(input("Enter num2:"))
s1=sum_of_two_num(num1,num2)
print(s1)

print("subraction operation using return statement")
def sumoftwonumm():
	sum=n1+n2
	return sum

n1=3
n2=4
sumoftwonumm()
s1=print(sumoftwonumm())

print("cub operation using funtion")
def  cub(n1):
	cub=(n1**3)
	print("Cub=",cub)

num1=2
cub(num1)
