import random



def loop(n,k):
	for i in range(0,n):
		print(k,end="")

loop(n=10,k="*\t")
print()
print("*",end="")
loop(n=9,k="\t")
print("*")
print("*",end="")
loop(n=9,k="\t")
print("*")
print("*",end="")
loop(n=4,k="\t")
print("WELCOME",end="")
loop(n=5,k="\t")
print("*")
print("*",end="")
loop(n=9,k="\t")
print("*")
print("*",end="")
loop(n=9,k="\t")
print("*")
loop(n=10,k="*\t")
print()
input("Press any key to start:")
print("\n"*50)


def mainmenu():
	print("WELCOME THE HOUSEING GAME:)")
	print("1.Rock,Paper,Scissors\n2.Cow And Bulls\n3.Exit")
	ch=int(input("Enter The Choice:"))
	if ch==1:
		print("\n"*50)
		rockpaperscissorsmenu()
	elif ch==2:
		print("\n"*50)
		cowsandbuyllsmenu()
	elif ch==3:
		print("THANK FOR VISIT:)")
	else:
		print("Invalid Choice:(")
		print("\n"*50)
		mainmenu()


def rockpaperscissorsmenu():
	print("WELCOME ROCK,PAPER,SCISSORS")
	print("1.Play\n2.Rule Of Game\n3.Return The Main Menu")
	ch=int(input("Ente The Choice:"))
	if ch==1:
		print("\n"*50)
		rockpaperscissors()
	elif ch==2:
		print("\n"*50)
		rockpaperscissorsrule()
	elif ch==3:
		print("\n"*50)
		mainmenu()
		print("\n"*50)
	else:
		print("\n"*50)
		print("Invalid Choice!")
		rockpaperscissorsmenu()
		print("\n"*50)

def cowsandbuyllsmenu():
	print("WELCOME COWS AND BULLS")
	print("1.Play\n2.Rule Of Game\n3.Return The Main Menu")
	ch=int(input("Ente The Choice:"))
	if ch==1:
		print("\n"*50)
		cowsandbuylls()
	elif ch==2:
		print("\n"*50)
		cowsandbuyllsrule()
	elif ch==3:
		print("\n"*50)
		mainmenu()
		print("\n"*50)
	else:
		print("\n"*50)
		print("Invalid Choice!")
		cowsandbuyllsmenu()
		print("\n"*50)


def rockpaperscissorsrule():
	print("Rock,Paper,Scissors Rule")
	print("1.You will be competing against the computer.")
	print("2.The player that scores 5 points first,will be declared the winner.")
	print("3.Player maximum 25 chance take it")
	print()
	print("Game Rules:")
	print("1.If the first player to choice the Rock,another second player to choice Paper, that case the second player geting the score.")
	print("2.If the first player to choice the Rock,another second player to choice Scissors, that case the first player geting the score.")
	print("3.If the first player to choice the Paper,another second player to choice Scissors, that case the second player geting the score.")
	print("4.If the both player to give the same choice, that case the second player no geting the score.")
	print("\n"*2)
	input("Enter Any Keys To Go Back")
	print("\n"*50)
	rockpaperscissorsmenu()


def rockpaperscissors():
	print("Note:-If you choice in Rock(Enter 0),Paper(Enter 1),Scissors(Enter 2),and Exit(Enter -1)")
	print()
	print("The Game Is Beggan!")
	user=0
	compt=0
	cnt=0
	choice=["Rock","Paper","Scissors"]
	while(user<5 and compt<5 and cnt<25):
		userch=int(input("Enter Your Choice:"))
		if userch==-1:
			print("Your conform to Exit(Enter Again -1),Either(Enter 9) ")
			n=int(input("Enter:"))
			if n==-1:
				print("Thank You!")
				return
			elif n==9:
				print("\n"*50)
				print("Lets Start!")
				continue
		comptch=random.choice([0,1,2])
		if (userch==0 and comptch==1):
			compt+=1
		elif (userch==0 and comptch==2):
			user+=1
		elif (userch==1 and comptch==0):
			user+=1
		elif (userch==1 and comptch==2):
			compt+=1
		elif (userch==2 and comptch==0):
			compt+=1
		elif (userch==2 and comptch==1):
			user+=1
		elif (userch==0 and compt==0):
			print("Draw!")
		elif (userch==1 and compt==1):
			print("Draw!")
		elif (userch==2 and compt==2):
			print("Draw!")
		else:
			print("Invalid No.")
			print("\n"*2)
			continue
		print("You:",choice[userch])
		print("Computer:",choice[comptch])
		print()
		print("Your Score:",user,"\tComputer's Score:",compt)
		print("\n"*2)
	if (userch>comptch):
		print("Congragulation! You Win!")
	elif (comptch>userch):
		print("Oops! You lose!")
	elif (userch==comptch):
		print("Match Is Draw!")
	print("\n"*2)
	input()
	print("\n"*50)
	mainmenu()

def cowsandbuyllsrule():
	print("Cow & Bulls Rules ")
	print("1.You are compet the against computer")
	print("2.The first player to take input then computer take the input in the game")
	print("3.The player take 4 input then computer take 4 input then match the both number who score more")
	print("4.Decleared Win Either You Lose")
	print("\n"*2)
	input("Enter Any Key To Go Back Menu")
	print("\n"*50)
	cowsandbuyllsmenu()

def cowsandbuylls():
	word=["rate","fail","cake","sore","tear","calm","rage","time","face","swan"]
	cnt=0
	while(cnt<15):
		s=input("Enter the string:")
		if s=="-1":
			print("Tank you!")
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
