# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	# pass
# 	l = []
# 	lst = []
# 	c=0
# 	if a ==[]:
# 		return []
# 	for x in a:
# 		c = 0
# 		i = a.index(x)
# 		for j in range(i,len(a)):
# 			if x != a[j]:
# 				break
# 			c+=1
# 		l.append((c,x))
# 	for i in l:
# 		if i not in lst:
# 			lst.append(i)
# 	print(list(lst))
# 	return(list(lst))
# lookandsay([3,3,8,-10,-10,-10])
  
	l = []
	lst = []
	c=1
	if a == []:
		return []
	# k = 0
	for x in range(len(a)):
		c = 0
		# print(a[x])
		for j in range(x,len(a)):
			if a[x] != a[j]:
				break
			c+=1			
		l.append((c,a[x]))
	# for i in l:
	# 	if i not in lst:
	# 		lst.append(i)
	for i in range(1,len(l)):
		print(l[i])
		# if i>i+1:
		# 	lst.append(i)
		# result = all(x < y for x, y in zip(i, i+1))
	# print(lst)
	
	return(list(lst))
lookandsay([3,3,8,3,3,3,3])
				