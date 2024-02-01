print("The break statement")
for i in range(0,5):
	if(i==5):
		break
	print(i)
print("Thank you :)")

print("The Prime number") #for else statement
num=int(input("Enter num:"))
for i in range(2,num):
		if(num%i==0):    
			print("Number is not prime") 
			break
else:
	print("Number is prime")
print("Thank you!")			
			
print("The continue statement")
n=int(input("Enter num:"))
for i in range(1,n+1):
	if(i%3==0):
		continue
	print(i)
print("Thank you!")

print("The pass statement")
num1=0
num2=2
if num1==0:
	pass #It is empty space
else:
	print("Result Division=",num2//num1)
	
	

