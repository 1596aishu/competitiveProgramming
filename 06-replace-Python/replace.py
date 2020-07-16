# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().
def strings(x,y,z):

	a=""
	for i in range(0+z,len(x)):
		if i != len(x)-1:
			a += x[i]+ y
		else:
			a += x[i]
	print(a)		
	return a
def fun_replace(s1, s2, s3):
	x = s1.split(s2)
	print(x)
	if(len(x[0])==len(s1)):
		print(s1)
		return s1
	else:
		y=""
		i=0
		if(len(x[0]) == 0):
			i = 1
			y += s3
		y += strings(x,s3,i)
		print(y)
		return y
