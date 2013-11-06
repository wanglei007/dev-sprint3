# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Lei Wang

#9.7

def checkFordouble(word, n):
	if n==0:
		return True
	if len(word)<2*n:
		return False 
	if word[0]==word[1]:
		return checkFordouble(word[2:],n-1)
	else:
		return False

def checkFor3Double(word):
	if len(word) < 6:
		return False
	i = 1
	while (i < len(word)) and (word[i-1]<>word[i]):
		i += 1
	if (i< len(word)-4) and checkFordouble(word[i+1:],2):
		return True
	elif (i< len(word)-7):
		return checkFor3Double(word[i+1:])
	else:
		return False



fin=open ('.\word.txt')
for line in fin:
	word = line.strip()
	if checkFor3Double(word):
		print word
