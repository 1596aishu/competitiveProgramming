# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	# print(num)
	s = ""
	num = sorted([int(x) for x in num])
	lst = num[::-1]
	for x in lst:
		s += str(x)
	# print(int(s))
	return int(s)
