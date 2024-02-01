

for i in range(0,4):
	for k in range(i,4):
		print("*\t",end="")
	for j in range(0,i):
		print("\t",end="")
	for h in range(0,4):
		for n in range(0,i):
			print("\t",end="")
		for v in range(i,4):
			print("*\t",end="")
	print()