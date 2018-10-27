import random
n=int(input("turns"))
choice=0
computerchoice=0
i=0
while i!=n:
	c=int(input("user turn"))
	result=0
	if(c==1):
		choice="rock"
	elif(c==2):
		choice="paper"
	else:
		choice="scissors"
	print("user turn: " ,choice)
	print("computer turn")
	computer=random.randint(1,3)
	if(computer==1):
		computerchoice="rock"
	elif(computer==2):
		computerchoice="paper"
	else:
		computerchoice="scissors"
	print("computerchoice:" ,computerchoice)
	if((c==1 and computer==2) or(c==2 and computer==1)):
		print("paper wins")
		result="paper"
	elif((c==1 and computer==3) or(c==3 and computer==1)):
		print("rock wins")
		result="rock"
	elif((c==2 and computer==3) or(c==3 and computer==1)):
		print("scissors wins")
		result="scissors"
	else:
		result=="x"
	if(result==choice):
		print("user wins")
	elif result== 'x':
		print("draw")
	else:
		print("computer wins")
	i=i+1
