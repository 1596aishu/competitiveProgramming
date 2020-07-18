# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	d = {}
	l = []
	l1 = []
	for i in s:
		if i not in l1:
			z = s.count(i)
			l1.append(i)
			if z == n-1:
				print(i)
				# return i
			l.append((z,i))
	l = sorted(l)
	# l = l.sort(reverse = True)
	print(l)

	# return 'a'


fun_kth_occurrences("helllo woorld", 2)