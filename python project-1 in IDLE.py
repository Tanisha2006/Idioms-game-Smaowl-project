

a=str(input('Kindly enter your name to start this game'))
print('Lets start the game',a,'!!!')

print('the idioms which have been given for your help. you have to guess the', 
		'idioms by thier meanings given by the computer to you\n\n Remmember to write the idioms as it is, as the game is case'
		"sensitive, Don't cheat as there are more difficult idioms in the next level")

print('1.A blessing in disguise\n',
'2.A dime a dozen\n',
'3.Adding insult to injury\n',
'4.Beat around the bush\n',
'5.Beating a dead horse\n')


i1='A blessing in disguise'
i2='A dime a dozen'
i3='Adding insult to injury'
i4='Beat around the bush'
i5='Beating a dead horse'

m1='A good thing that initially seemed bad'
m2='Something that is very common,not unique' 
m3='To make a bad situation even worse'
m4='Avoid sharing your true viewpoint or feelings because it is uncomfortable'
m5='Giving time or energy to something that is ended or over'

one=1


print(m1)

player = str(input('ENTER YOUR ANSWER--\n'))


if  player==i1:
	print('You won ',a,'.You Got 1 point.\n\n') 
else:
	print('Sorry You lost')

print(m2)

player = str(input('ENTER YOUR ANSWER--\n'))


if player==i2:
	print('You won',a,'.You got 1 point\n\n')
else:
	print('Sorry You lost')

print(m3)

player = str(input('ENTER YOUR ANSWER--\n'))

if  player==i3:
	print('You won ',a,'.You got 1 point.\n\n') 
else:
	print('Sorry You lost')

print(m4)

player = str(input('ENTER YOUR ANSWER--\n'))

if player==i4:
	print('You won ',a,'.You got 1 point.\n\n')
else:
	print('Sorry You lost')

print(m5)

player = str(input('ENTER YOUR ANSWER--\n')) 

if player==i5:
	print('You won ',a,'.You got 1 point.\n\n')
else:
	print('Sorry You lost')


raw_data=int(input('Enter the score of question 1: '))
raw_mat=int(input('Enter the score of question 2: '))
raw_score=int(input('Enter the score of question 3: '))
raw_av=int(input('Enter the score of question 4: '))
raw_tt=int(input('Enter the score of question 5: '))
result = raw_data + raw_mat + raw_score + raw_av + raw_tt
print('Your final score is',result)


if  result >=3:
	print('Congratulations!! You moved on to the next level\n\n')
	print('The rules for the second level are that you have to write the meanings of the idioms given to you,\n') 
	('The following are your options and answer to the questions\n\n')
	s1= 'Cut somebody some slack'
	s2='Let someone off the hook'
	s3='Give someone the benefit of the doubt'
	s4='Miss the boat'
	s5="That's the last straw"

	t1='To not be so critical'
	t2='Fail to take advantage of an opportunity'
	t3='Trust what someone says'
	t4='When patience has ran out'
	t5='To not hold someone responsible for something'

	print(s1)

	answer = str(input('ENTER YOUR ANSWER--\n'))


	if  answer==t1:
		print('You won ',a,'.You Got 1 point.\n\n') 
	else:
		print('Sorry You lost')

	print(s2)

	answer = str(input('ENTER YOUR ANSWER--\n'))


	if answer==t5:
		print('You won',a,'.You got 1 point\n\n')
	else:
		print('Sorry You lost')

	print(s3)

	answer = str(input('ENTER YOUR ANSWER--\n'))

	if  answer==t3:
		print('You won ',a,'.You got 1 point.\n\n') 
	else:
		print('Sorry You lost')

	print(s4)

	answer = str(input('ENTER YOUR ANSWER--\n'))

	if answer==t2:
		print('You won ',a,'.You got 1 point.\n\n')
	else:
		print('Sorry You lost')

	print(s5)

	player = str(input('ENTER YOUR ANSWER--\n')) 

	if player==t4:
		print('You won ',a,'.You got 1 point.\n\n')
	else:
		print('Sorry You lost')


	data=int(input('Enter the score of question 1: '))
	mat=int(input('Enter the score of question 2: '))
	score=int(input('Enter the score of question 3: '))
	av=int(input('Enter the score of question 4: '))
	tt=int(input('Enter the score of question 5: '))
	your = raw_data + raw_mat + raw_score + raw_av + raw_tt
	print('Your final score is',your)

	if your >= 3:
		print('Great you have done well in both the levels\n')
		def add(add):
			average=result+your/2
			print('The average score of both the rounds is',average)
			print('This is the end of the game hopefully you had fun')
		add(add)
	else:
		print('Sorry you lost in this round but you did well in the first one')
		print('This is the end of the game hopefully you had fun')
else:
	print('Sorry you need to play this level again if you want to move onto the next level')








	









