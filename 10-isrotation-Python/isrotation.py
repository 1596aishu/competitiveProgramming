# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(str1, str2):
	# Your code goes here
	# pass
	sting=""
	str3 = str2[:1:]
	for x in str1:
		if str3 != x:
			sting+=x
		if str3==x:
			break
	for y in range(len(str1)):
		if str1[y]==str3:
			str4=str1[y::]
	result = str4+sting
	print(result)
	if result==str2:
		return True
	else:
		return False