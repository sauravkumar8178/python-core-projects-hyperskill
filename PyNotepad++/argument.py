print("Passing argument")
def div(n1,n2):      #passing argument it mean that the order of parmeters(n1,n2) are equal to the argument(num1,mnum2)
	div=n1//n2
	return div

'''num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
s1=div(num1,num2)
print(s1)

print("Defualt argument")      #Defualt argument it mean that the user call the function in body in one value(num1) to use the defualt value because not 
def addition(n1,n2=0,n3=0):    #assign the defualt value in other the variable to show the garbage in the operation so it is use to defualt value 
	add=n1+n2+n3                     # note:- always the assign the defualt value in the right side to start for eg. n1,n2=0,n3=0 not start left side
	print("Addition=",add)
	return add

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
s=addition(num1)
print("s",s)
s1=addition(num1,num2)
print("s1",s1)
s2=addition(num1,num2,num3)
print("s2",s2)
s3=addition(num1,num3)
print("s3",s3)

print("Keyword argument")
def mult(n1,n2,n3,n4):
	mult=n1*n2*n3*n4
	return mult

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
num4=int(input("Enter num4:"))
s=mult(n2=num1,n3=num2,n4=num3,n1=num4) #Many time user not reminder the order of parameter function so that case we can use the user the same line 
print(s)'''

print("Aribitrary argument")
def mult(*num):
	mult=1
	for n in num:
		mult=mult*n
	return mult                #for for read the s,s1,s2,s3,s4 result and then perform operation.
                               #It is mainly used to define infinit arguments so it is used aribitrary argument(*parameter)
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
num4=int(input("Enter num4:"))
s=mult(num1)
s1=mult(num2,num3,num4)
s2=mult(num2,num4)
s3=mult(num3)
s4=mult(num1,num2,num3,num4)
print(s)
print(s1)	
print(s2)
print(s3)
print(s4)
