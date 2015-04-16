# Write a function that takes a set of n length and return its power set.

# [ ] --> [ [ ] ]

# [1] --> [ [ ], [1] ]

# [1,2] --> [ [ ], [1], [2], [1,2] ]

# [1,2,3] --> [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]

# Let's assume the constraints for lists and sets are the same; there will be no duplicates.

def power_set(a_set):
	
	if len(a_set) == 0:
		return [a_set]
	
	p_set = power_set(a_set[:-1])
	
	for i in range(len(p_set)):
		p_set[i].append(a_set[-1])
	
	return power_set(a_set[:-1]) + p_set

