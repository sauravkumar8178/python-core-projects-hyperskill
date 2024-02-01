'''print("Creat The New File")
file=open("D:\Python\myfile.txt","w")  #It is creat the file with ext. flie name.txt And "w" mean write the data in file.
n=input(str("Write Data:"))
file.write(str(n))
file.write("Welcome to Python college\n")
file.write(str(1000))
file.close()
print()

print("Accessing Aother Ext. File & Reading The File")
file=open("D:\Python\sets.py","r")  #It is accessing the file user take input D:\Python\filehandling.py this is example.
filedata=file.readlines()    #It is work on any file. Syntax:-user input- path\working file name(filehandling).ext
print(filedata)          #It show the all the file contain.It mean all lines are show in output
file.close()
print()

print("Read Text File & Manipulating Or Converting string To Integer")
file=open("D:\Python\myfile","r")   #"r" mean the file reading.
print(file.readline(7))    #It is read the 7 character of string
print(file.readline(),end="")     #It read the 2nd line and remove more space it mean that line by line shows
print(int(file.readline())+2)      #It read the 3rd line and also To convert string to integer So to perform the add operation 1000+2=1002 (And also covert & manipulating this file.)
print(file.readlines())         #It is creat the empty list because they no more line are present in this file
file.close()
print()'''

'''print("Take The Binary Data")
f=open("D:\Python\binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()'''

'''print("File Operations")
print("File Positions")
file=open("D:\Python\myfile.txt","w")  # In the reading mode("r") it is seek the show the words of file. 
print(file.tell())      #It is used to tell the position the cursire are present in file
print(file.seek(7,0))   #It is used to move the cursire in current file Syntax:-file.seek(offset,from) offset->when you move cursire,      
file.write("World")      #form->where you count cursire like- 0->beginning of file, 1->current position of file, 2->end of file.
file.close()
print()'''

print("Directory Of Filehandling")
import os
import os D:\Python\Myfolder
os.mkdir("Myfolder")
