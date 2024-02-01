print("The Bitwise Operator")
x=int(input("Enter the vlaue of x:"))
y=int(input("Enter the vlaue of y:"))
print("Result AND:",x&y)
print("Result OR:",x|y)
print("Result NOT:",~x) #It is also known as 1's complement 
''' 
Important Notes:-
x=2 It mean binary No. 010
that convert ~x=101
calculate that ~x= -4+2-1
               ~x= -3 Answers
			   they are valid on all logic gate
'''			   
print("Result XOR:",x^y)
print("Result Right Shift:",x>>1)
'''
x=5
x=0101
x>>1=0010
x=2 Right Shift
'''
print("Result left Shift:",x<<1)
'''
x=5
x=0101
x<<1=1010
x=10
'''
print("Result 2's complement:",~x+1)
# It is (+1) one add on 1's complement