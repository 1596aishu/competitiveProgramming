# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	# pass
	c = len(a)
	if(c>0):
		if(c%2!=0):
			return a[(c-1)//2]
		else:
			return (a[(c//2)-1]+a[c//2])/2
	else:
		return None