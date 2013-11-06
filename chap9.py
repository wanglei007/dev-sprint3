# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Lei Wang

#9.1

fin=open ('.\word.txt')
for line in fin:
	word = line.strip()
	if len(word) > 20:
		print word

#9.2

def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
			
	return True

print has_no_e('world')
print has_no_e("hello")

#9.3

def avoids(word, forbids):
	for letter in forbids:
		if letter in word:
			return False
	return True

forbids = raw_input("give me all your forbidden letters: ")
word = raw_input("give a word you want to test: ")
print avoids(word, forbids)


#find the combo of 5 that exludes least

def avoid_count(letter):
	fin=open ('.\word.txt')
	count = 0
	for line in fin:
		word = line.strip()
		if avoids(word, letter):
			count +=1
	return count

letter = 'a'
while letter <= 'z':
	print letter, avoid_count(letter)
	letter = chr(ord(letter)+1)

#9.4

def uses_only(word, limit):
	for letter in word:
		if letter not in limit:
			return False
	return True

print uses_only('world', 'dfas')
print uses_only('asdfdaf', 'asdf')


