# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Lei Wang
#8.12 ROT13

def rotate_word(oldStr, n):
	if not oldStr.isalpha():
		print "not a valid string"

	newStr = ''

	for letter in oldStr:
		newOrd = (ord(letter)-ord('A')+n) % 52 + ord('A')
		newStr += chr(newOrd)

	print newStr


