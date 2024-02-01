print("Anonymous function")
Sum_of_two_num=lambda n1,n2:n1+n2          #In anonymous function the expression(n1+n2) are return the value in function name(Sum_of_two_num)
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(Sum_of_two_num(n1=num2,n2=num1))

print("Scope & Lifetime Variable")
def sumoftwonum():
	sum=n1+n2               #Local variable are those variable which inside the function like sum. Local variable are remove memory location then excuted function
	return sum              #Global are those variable which are declaraed the body like n1,n2. Global variable are remove momory location then excuted body
                            #Always global variable more than prefrence in the local variable
n1=3
n2=4
print(sumoftwonum())

