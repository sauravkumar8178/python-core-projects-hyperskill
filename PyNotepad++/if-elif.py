print("The if-elif Ladder statement\n")
print("Use The Sign To Perform The calculation:\n Addition(+)\n Substraction(-)\n Multiplicatino(*)\n Division(/)\n Modulus(%)\n Expoential(**)\n") 
value1=int(input("Enter value1:"))
Sign=(input("Enter Sign:"))
value2=int(input("Enter vaue2:"))
print()
if(Sign=='+'):
	print("Result Addition=",value1+value2)
elif(Sign=='-'):
	print("Result Substraction=",value1-value2)
elif(Sign=='*'):
	print("Resilt Multiplicatino=",value1*value2)
elif(Sign=='/'):
	if(value2==0):
		print("Division is not possible :(")
	else:
		print("Result Division=",value1/value2)
elif(Sign=='%'):
	print("Result Modulus/Reminder=",value1%value2)
elif(Sign=='**'):
	print("Resilt Expoential=",value1**value2)	
else:
	print("Invalid input :(")
print("Thank you!")
print()


print("The Neste if statement\n")
num=int(input("Enter number"))
if(num>1000):
	if(num%10==0):
		if(num%4==0):
			if(num/2):
				print("Good :)")
			else:
				print("Invalid")
else:
	print("not good")