print("Find The ASCII Value")
ch=str(input("Enter the character:"))
print("ASCII values of",ch,"is:",ord(ch)) #find ASCII value
print()

print("Character call given string")
s="hello"
print(s[-1])               #To call the character in the string in forward direction string read 0=h,1=e,2=l,3=l,4=o
print(s[0])
print(s[2])                #To call the character in the string in backward direction string read -1=o,-2=l,-3=l,-4=e,-5=h
print(s[-2])               #sntax:-variable[number of character]
print()

print("Basic Operator")
s="Hello"
s1="World"
jion=s+" "+s1   #it jion the two string
print("Concatenation:",jion)
repreat=jion*4   #it repreat the string to give number
print("Replication:",repreat)
print()

print("Membershipe operator")
print("Using in Membershipe")
s="Hello"
if "ell" in s:   #in Membershipe are show that character are present
	print("Present")
else:
	print("Not")
print("Using not in Membershipe")
s1="World"
if "orl" not in s1:  #not in Membershipe are show that character are not present
	print("Right :)")
else:
	print("Wrong :(")
print()

print("Relational & Comparision")
if "hello"<"world": #In relational operator (<,>,=<,=>,!=,==) are used to comparision in the based on ASCII like Book value 65111111107 are the compared that string
	print("right :)")
else:
	print("wrong :(")