# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	if street == 0: 
		return 0
	x = street%8
	# print(x)
	if x<=4: 
		print(street - x)
		return street - x
	else:
		if street==x:
			print(street - x) 
			return 8
		else:
			print(street + x)
			return street + x

# fun_nearestbusstop(4)
# fun_nearestbusstop(8)
# fun_nearestbusstop(12)
# fun_nearestbusstop(6)
