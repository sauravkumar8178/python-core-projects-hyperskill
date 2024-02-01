print("Slice String\Slicing Notation String")
print()
print("Accessing the character")
s="Hello World!"      # password 8860@singh
print(s[0:4])         #4 is not include beause It is start to 0,1,2,3 it count 4 So that case 4 are not include 3 are include. (forward)
print(s[-4:-1])       #(-1) not include because it start to -2,-3,-4 it count 3 so that case (-1) are not include (-2) are include. (backward)
print(s[0:11:2])       #it case the 2 or more multiple of 2 place accessing the element like 2,4,6,8......
print(s[-4:-1:2])
print(s[::2])
print(s[1::])
print(s[1:])
print(s[:3]) 
print()
print("Negative Way")
s1=input("Enter the string:")
print(s1[-len(s1):-1])
print(s1[-len(s1)::])
print(s1[::-1])       #It's read that like "Hello" output-> is "olleH"
print()

print("Functinon string & Method")
s2=input("Enter the string:")
print(s2.capitalize())  #It's not set the parameter like (0,5) & It work the first letter of sentence to convert big letter(hello string -> Hello string)
print(s2.count("l",0,len(s2))) #It set parameter are allow.
print(s2.endswith("llo",0,len(s2)))  #It check the string("llo") are present in(shows the true) / either not present(shows the false)
print(s2.find("llo",0,len(s2))) #It check the string(llo) which number of place then show the place number.
print(s2.find("aaa",0,len(s2))) #In the case the string(ooo) are not present then it shows -1.
print(s2.index("llo",0,len(s2))) #It work same to find function but In csae the input not match then show the error 
#like (s2.index("aaa",0,len(s2))) s2=hello. then show error
print(s2.isdigit())  #In case the only digit are present it show true either false
print(s2.isalnum())  #In case the alpha,num,are least one character present it show ture either false
print(s2.isalpha())  #In case the only alpha are present it show true either the false.
print(s2.islower())  #In case the all character are small the show the ture either false
print(s2.isupper())  #"    "    "   "    "       "    big  "   "     "   "    "      "
print(s2.isspace())  #In case at least one space are present it show the true either false
print(s2.upper())    #It convert all the letter are big
print(s2.lower())    #It convert all the letter are small
print(s2.swapcase()) #It case the small to big & big to small are convert the character
print(s2.lstrip())   #It case the all the whitespace"           hello string" are remove output-hello string
print(s2.rstrip())   #It creat the any word,&sentence are double
print(s2.startswith("h",0,len(s2))) #It can use sentence start with "h" then show the true either false
print()

print("Function programme")
s3=input("Enter the string:")
if s3.isdigit():
	print("digit are  present")
else:
	print("digit are not present")
print()

print("Travering String")
s4=input("Enter the string:")
for ch in s4:
	print(ch)
s5=input("Enter the string:")
for i in range(0,len(s5)):
	print(s5[i])      #It accessing each character using(s5[i])
print()

s6=input("Enter the string:")
ncount=0
acount=0
scount=0
for ch in s6:
	if s6.isdigit():     #It accessing each character it is true then operatio perform like- ncount=0+1=1 again check another character it false go the other
		ncount+=1
	elif s6.isalpha():
		acount+=1
	elif s6.isspace():
		scount+=1
	else:
		continue
print(ncount)
print(acount)
print(scount)

	



