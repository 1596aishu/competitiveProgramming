# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	
	num = [int(d) for d in str(hand)]
	print("(")
	for x in len(num):
		print(str(num[x]))
		if(x == len(num)-1)
	print(")")

handtodice(123)
