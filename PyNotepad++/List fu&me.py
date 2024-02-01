print("List Function & Method")
n=int(input("Enter Input:"))
lst=[int(input("Enter element:"))for i in range(0,n)]
print(lst)
print(max(lst))   #It is used to read the element of big element in case the string then show that error\first element
print(min(lst))   #It is used to read the element of small element in case the string then show that error\last element
print(lst.count(2))  #It is used to count the give number how time are present like count(2) and user input 2,2,2,2 show output 4
print(lst.index(2))    #It is check the value 2 in which place.
print(lst.reversed())   
print(sorted(lst))
#print(lst.sort(reverse=True))
print()

print("List Comprehensions")
sq=[]
for i in range(1,11):
	sq.append(i**i)
print(sq)
print()

s=[i**i for i in range(1,11)]
print(s)
print()

print("Traversing List")
l=[]
n=int(input("Enter Input:"))
for i in range(0,n):
	val=int(input("Enter element:"))
	l.append(val)
print(l)
print()

n=int(input("Enter Input:"))
l=[int(input("Enter element:"))for i in range(0,n)]
print(l)
print()

print("Accessing Element")
n=int(input("Enter Input:"))
l=[int(input("Enter element:"))for i in range(0,n)]
print(l)
for ele in l:
	print(ele)
print()

print("Function Programme")
def linearsearch(k,lst):
	for ele in lst:
		if k==ele:
			return True
	else:
		return False

n=int(input("Enter Input:"))
list=[input("Enter element:")for i in range(0,n)]
print(list)
key=input("Enter Key:")
val=linearsearch(key,list)
print(val)
print()

print("Tuples")

'''1. Tuples is same to list but It is not imutable
like kello not change hello
2.So It is more protected in campare to list because it is not imutable
3.  Syntax:-
		t1=(1,2,3,)
		t2=tuple((1,2,3,4...))
4. compare function are change in tuples.'''
