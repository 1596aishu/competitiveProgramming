# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	c = ""
	while x!=0 and y!=0:
		if len(x)>1 and len(y)>1:
			r = x%10
			print(r)
			s = y%10
			print(s)
			if r+s>9:
				c += str((r+s)%10)
			x = x//10
			y = y//10
		else:
			if r+s>9:
				c+=str((r+s)%10)
			else:
				c= str(r+s)
	c = c[::-1]
	# print(int(c))
	return c
fun_carrylessadd(121,0)

