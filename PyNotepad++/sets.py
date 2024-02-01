'''print("Member Operator")  #it is same to dictionary but sets it is unorder collection and repreation not allow.
s=input("Enter string:")
cunt=0
n=int(input("Enter number of chars:"))
spcl_chars={input("Enter the element:")for i in range(0,n)}
print(spcl_chars)
for ch in s:
	if ch in spcl_chars:
		cunt+=1
print(cunt)
print()'''

print("Method Sets")
s={}
n=int(input("Enter No. Input"))
s={input("Enter element:")for i in range(0,n)}
print(s)
#print(s.add(9))   #It is add the given element in last in sets section.
#print(s.clear())   #It is remove the all the elemnet in set it creat the empty set
'''s1={}
s1=s.copy()        #It is copy to one sets to another sets
print(s1)'''
s2={}
n1=int(input("Enter Input2:"))
s2={input("Enter element:")for i in range(0,n1)}
print(s2)
'''print(s.union(s2))  #It is used to math union function it creat the both element are include in one set but repreation not allow
#print(s.union_update(s2))  #It is used stored the values of union
print(s.intersection(s2)) #It is used intersection the two sets it mean that common element in both sets is intersection
#print(s.intersection_update(s2))  #It is used to stored in intersection values'''

