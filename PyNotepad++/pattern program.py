print("Half Pyramid")
n=int(input("Enter No. Of Input"))
for i in range(0,n):
	for j in range(0,i+1):
		print("*",end="")
	print()

print("Inverted Half Pyramid")
for i in reversed(range(0,n)):
	for j in range(0,i+1):
		print("*",end="") 
	print()
print()

print("Mirror of Inverted Half Pyramid")
for i in range(0,n):
	for j in range(0,i):
		print(" ",end="")
	for k in range(i,n):
		print("*",end="")
	print()
print()	
	
	
print("Truple Nested Loop")
for i in range(0,n):
	for j in range(0,n):
		for k in range(0,n):
			print("*",end="")
		print()
	print()
	
