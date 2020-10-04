import random,math,time

#game rules
print('welcome to number guessing game!')
time.sleep(1)
print('To play game,Clearly follow rules..')
time.sleep(1)
print('1.Enter your details')
time.sleep(1)
print('2.You should give the range between which numbers, you wanna guess')
time.sleep(1)
print('3.Try to give larger range.(ex:0-100)')
print('4.You will be given limited number of attempts to guess')
time.sleep(1)
print('5.If you guessed with in the chances ,then you did it!')
time.sleep(1)
print('6.If not you lost!')

#user details
name=input('Enter your name:')
#user range inputs
lower=int(input('Enter lower bound(ex:0):'))
upper=int(input('Enter upper bound(ex:100):'))

#random guessing number generation between lower and upper
guessnum=random.randint(lower,upper)

#generating number of choices
choices=round(math.log(upper-lower+1,2))
print('you have',choices,'chances')

#logic
count=0
while count<choices:
	count+=1
	guess=int(input('Guess the number:'))
	if guess==guessnum:
		print('Congratulations!')
		print(name,'won in',count,'attempts')
		break
	elif guess<guessnum:
		print('Try Again! You guessed too small')
	elif guess>guessnum:
		print('Try Again! You guessed too large')

# user choices are more than given choices	
if count==choices:
	print('The Guess Number is',guessnum)
	time.sleep(1)
	print('Better Luck Next Time',name,'!')	


