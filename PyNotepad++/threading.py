from _thread import start_new_thread
from time import sleep
threadID=1
waiting=2

def factorial(n):
	global threadId
	rc=0
	if n<1:
		print("{}: {}".format('\nThread',threadID))
		threadId+=1
		rc=1
	else:
		returnNumber=n*factorial(n-1)
		returnNumber=n*factorial(n-1)
		print("{} != {}".format(str(n),str(returnNumber)))
	return rc

start_new_thread(factorial, (5, ))
start_new_Thread(factorial, (4, ))

print("Waiting for thread to return...")
sleep(waiting)
