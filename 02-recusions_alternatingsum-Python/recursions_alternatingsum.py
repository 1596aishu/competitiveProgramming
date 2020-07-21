# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def alternatingSum(L):
	j = -1
	sum = 0
	for i in L:
		sum= sum+(i*(-j))
		j = j * (-1)
	# print(sum)
	return sum 


def fun_recursions_alternatingsum(l): 
	L = len(l)
	# i = 0
	if L>1:
		return alternatingSum(l)
	else:
		return 0

# fun_recursions_alternatingsum([5,3,8,4])