print("Manipulating And Accessing Dictionary")
d={1:"Shivam",2:"Roshan",3:"Deeple",4:"Kaala",5:"Dobhi"}
print(d)
print(d[3])
d[3]="Dobhi"    #Only value(like:-Shivam,Roshan etc.) are change (manipulating) and keys(like:-1,2,3,etc) are not change. 
print(d[3])     #Accessing any dictionary to call the key(like:- [3],[5],etc.)
print()

print("Function of dictionary")
'''class_list=dict()
data={input('Enter the name & score separated by ":" ')}
temp=data.split(':')
class_list[temp[0]]=int(temp[1])
for key,value in class_list.items():
	print('Name: {}, Score: {}'.format(key, value))'''
	
'''mydict = {}
for totnum in range(0,int(input('Input the total number'))):
    a, b = input('Enter the key value pair').split(":")
    mydict[a] = [b]
print(mydict)'''


d={1:"ello",2:"dello",3:"rello",4:"sello",5:"nello"}
d2={1:"Shivam",2:"Roshan",3:"Deeple",4:"Kaala",5:"Dobhi"}
print(len(d))
#print(cmp(d,d2))
print(str(d),str(d2)) #It is converted the string.
print()

print("Method Dictionary")
d={1:"ello",2:"dello",3:"rello",4:"sello",5:"nello"}
print(d.keys())  #It is show the all keys are present in given dictionary output:- dict_keys([1,2,3,4,5])
print(d.values()) #It is show the all values are present in given dictionary output:- dict_values(['ello', 'dello', 'rello', 'sello', 'nello'])
print(d.items())   #It show the all items mean that keys and values output:-dict_items([(1, 'ello'), (2, 'dello'), (3, 'rello'), (4, 'sello'), (5, 'nello')])
#print(d.clear())   #It is clear all the dictionary return empty dictionary
d2={1:"Shivam",2:"Roshan",3:"Deeple",4:"Kaala",5:"Dobhi"}
d.update(d2)
print(d) #It is remove the dictionary(d) and put the items of the dictionary(d2) then print the d show the d2 items (it is allow this case)
d3={}
d3=d.copy()
print(d3)  #It copy the d items in d3 dictionary output:-{1:"ello",2:"dello",3:"rello",4:"sello",5:"nello"}
print(d.get(4))  #It is used to accessing the key value but key are not present it show the Non
#print(d.has_key(7))   #It keys are present in dictionary it show true and false
t=(1,2,3,4,5,6)
d3=d3.fromkeys(t,0)
print(d3)   #It make the items in {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0} zero is add in t(1,2..6)keys and stored in d3 dictionary
d3=d3.fromkeys(t)
print(d3)      #It shows onlt t output:-{1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
#d4={6:"oop",7:"ai"}
#d=d.update(d4)    # not supported in this case
#print(d)
print()

print("Membership Operator")
d={1:"Shivam",2:"Roshan",3:"Deeple",4:"Kaala",5:"Dobhi"}
print("Use in")
if 2 in d:
	print("True")
else:                                 #It is only allow the keys
	print("False")
print("Use not in")
if "shivam" not in d:
	print("True")
else:
	print("False")
print()

print("Traversing the dictionary")
d={1:"Shivam",2:"Roshan",3:"Deeple",4:"Kaala",5:"Dobhi"}
for keys in d:
	print("Roll No.:",keys)  #It show the keys one by one 
	print("Name:",d[keys])    #It show the keys values one by one
	print()