# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	a = ""
	if(len(s1)==len(s2)):
		for i in range(len(s1)):
			a+=s1[i]+s2[i]
		return a
	elif(len(s1)>len(s2)):
		for i in range(len(s2)):
			a+=s1[i]+s2[i]
		a+=s1[len(s2):len(s1):1]
		return a
	elif(len(s1)<len(s2)):
		for i in range(len(s1)):
			a+=s1[i]+s2[i]
		a+=s2[len(s1):len(s2):1]
		return a
	return ""
	