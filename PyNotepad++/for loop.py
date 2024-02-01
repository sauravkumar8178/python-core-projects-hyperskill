n=int(input("Enter n:"))
for i in range(0,n):
	print(i)
print("Thank you!")

n=int(input("Enter n:"))
for i in range(0,n):
	for j in range(0,i+1):
		print(j,end="")
	print()
print("Thank you!")