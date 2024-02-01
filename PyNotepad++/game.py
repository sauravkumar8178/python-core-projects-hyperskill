import random

for i in range(0,10):
	print("*\t",end="")
print()
print("*",end="")
for i in range(0,9):
	print("\t",end="")
print("*")
print("*",end="")
for i in range(0,9):
	print("\t",end="")
print("*")
print("*",end="")
for i in range(0,4):
	print("\t",end="")
print("WELCOME",end="")
for i in range(0,5):
	print("\t",end="")
print("*")
print("*",end="")
for i in range(0,9):
	print("\t",end="")
print("*")
print("*",end="")
for i in range(0,9):
	print("\t",end="")
print("*")
for i in range(0,10):
	print("*\t",end="")   #The Cover Page.
print()
input("Press any key to start:")
print("\n"*100)    #It created the new line in the 100 times because it clear thr screen.

def mainmenu():
	print("1.Rock Paper Scissors\n2.Cows and Bulls\n3.Exit")
	ch=int(input("Enter The Choices:"))
	if ch==1:
		print("\n"*50)
		rockpaperscissorsmenu()
	elif ch==2:
		print("\n"*50)
		cowandbullsmenu()
	elif ch==3:
		print("Thanks You For Visit This Game:)")
	else:
		print("Invalid choice!")
		print("\n"*50)
		mainmenu()

def rockpaperscissorsmenu():
	print("WELCOME THE ROCK,PAPER,AND SCISSORS")
	print("1.Paly\n2.Rules Of Game\n3.Return to Main Menu")
	ch=int(input("Enter The Choices:"))
	if ch==1:
		print("\n"*50)
		rockpaperscissors()
	elif ch==2:
		print("\n"*50)
		rockpaperscissorsrules()
	elif ch==3:
		print("\n"*50)
		mainmenu()
		print("\n"*50)
	else:
		print("Invalid Choices!")
		print("\n"*50)
		rockpaperscissorsmenu()
		
def cowandbullsmenu():
	print("WELCOME THE COW AND BULLS")
	print("1.Paly\n2.Rules Of Game\n3.Return to Main Menu")
	ch=int(input("Enter The Choices:"))
	if ch==1:
		print("\n"*50)
		cowandbulls()
	elif ch==2:
		print("\n"*50)
		cowandbullsrules()
	elif ch==3:
		print("\n"*50)
		mainmenu()
		print("\n"*50)
	else:
		print("Invalid Choices!")
		print("\n"*50)
		cowandbullsmenu()
		
def rockpaperscissors():
	print("WELCOME TO ROCK,PAPER,AND SCISSORS")
	print("You will be competing against the computer.The player that scores 5 points first, will be declared as the winner")
	print("If your chooices is Rock,please Enter 0")
	print("If your chooices is Paper,please Enter 1")
	print("If your chooices is Scissor,please Enter 2")
	print("If your wish is Exit,please Enter -1")
	user=0
	compt=0
	cnt=0  #In the case the user and compt both are same input in many time the loop are run infinit time that cause to use count(cnt=0) it is fixid the loop like cnt=25 
	choice=["Rock","Paper","Scissors"]
	while(user<5 and compt<5 and cnt<25):
		cnt+=1
		userch=int(input("Enter your choice:"))
		if userch==-1:
			print("Thank You")
			break
		comptch=random.choice([0,1,2])
		if userch==0 and comptch==1:
			compt+=1
		elif userch==0 and comptch==2:
			user+=1
		elif userch==1 and comptch==0:
			user+=1
		elif userch==1 and comptch==2:
			compt+=1
		elif userch==2 and comptch==0:
			compt+=1
		elif userch==2 and comptch==1:
			user+=1
		print("You:",choice[userch])
		print("Computer:",choice[comptch])
		print("Your Score:",user,"\tComputer Score:",compt)
	if(user>compt):
		print("Congragulations You win!")
	elif(compt>user):
		print("Oops!Sorry you lose. Better luck next time!")
	else:
		print("Match Draw")
	mainmenu()
	
	
def cowandbulls():
	words=["rate","fail","cake","sore","tear","calm","rage","time","face","swan"]
	rand=random.randrange(0,10)
	word=words[rand]
	cnt=0
	while(cnt<15):
		s=input("Enter the string:")
		if s=="-1":
			print("Tank yoou!")
			return
		cows=0
		bulls=0
		chars=0   #It is used to check characters are present in the user given inputs.
		for c in s:
			if c in word:
				chars+=1
		for i in range(0,4):
			if s[i]==word[i]:
				bulls+=1
		cows=chars-bulls
		print("Cows:",cows,"\tBulls:",bulls)
		if bulls==4:
			print("Congragulations!You Win!")
			mainmenu()
		cnt+=1
	print("Oops!Maximum guess limit rearched!")
	mainmenu()

mainmenu()



	