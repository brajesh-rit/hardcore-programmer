def gridTraveler (m , n, memo = {}):
	com_key = str(m) + ',' + str(n)
	if (com_key in memo ):
		return memo[com_key]
	if (m == 1 and n == 1):
		return 1
	if (m == 0 or n == 0):
		return 0
	memo[com_key] = gridTraveler(m - 1, n, memo) + gridTraveler(m , n -1, memo)
	return memo[com_key]


print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(18, 18))



