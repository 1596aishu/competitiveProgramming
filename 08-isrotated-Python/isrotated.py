# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	pass
	# str3= list(str1)
	# str3 = str1[len(str1)-1:len(str1):]+str1[:len(str1)-1:]
	sting=""
	str3 = str2[:1:]
	for x in str1:
		if str3 != x:
			sting+=x
		if str3==x:
			break
	print(sting)




	
isrotated("12345","54321")
  