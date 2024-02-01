print("Simple list")
l=[]
n=int(input("No. Of Input:"))
for i in range(0,n):
	ele=input("Enter Element:")
	l.append(ele)
print(l)
print("Accessing Element NO. 6:",l[6])
ch=input("Enter change element of 6 place:")
l[6]=ch
print("After change element:",l[6])
print(l[0:3])
print(l[0:6:3])
print(l[-6:-1:2])
print(l[-6:-1])
print(l[::-1])
print(l[-5::])
print(l[:5])
print(l[2:])
print(l[-4:])
print(l[:-1])
print("Thank you:)")
print()

print("Nested list")
l=[98,90,56,[0,'a','91'],78]
print(l)
print(l[3][2])
print()

print("Manipulating list element")
n=int(input("Enter Input:"))
list=[input("Enter element:")for i in range(0,n)]
print(list)
list.append("12") #It is add single element of the list in last section
print("add:",list)
ele=input("Enter values:")
list.extend(ele)  #It is adding one more element of each characters in the list in last section 
print("Extend:",list)
list.insert(4,100)   #It is used to the add the value(100) in place No.4 it is not replaced
print(list)
l1=['hello',67,98,]
l2=list+l1
print(l2)
l3=l1*4
print(l3)
print()

print("Delecting Orperation")
n=int(input("Enter Input"))
l8=[input("Enter the element:")for i in range(0,n)]
print(l)
del l8[2]  #It is used to delecting one element in given place No.
print("Delecting one element:",l)
del l8[0:len(l)]
print("delecting one more element:",l)
l8.clear()   #It is clear the all the list. It mean cearted the empty list.
print(l)
#l.remove(23)
#l.pop(2) 