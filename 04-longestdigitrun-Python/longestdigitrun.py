# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	# pass
	n = str(n)
	lst = []
	c = 1
	for i in range(1,len(n)):
		for j in range(len(n)):
			if n[j] == n[i]:
				c=c+1
		lst.append((n[i],c))
	print(lst)	
longestdigitrun(1177737321)