def canSum1(target, numbers):
	if (target == 0):
		return True
	if (target < 0):
		return False
	result = False
	for num in numbers:
		if num == 0:
			return True
		result = result or canSum1(target - num, numbers)
	return result


def canSum2(target, numbers):
	if (target == 0):
		return True
	if (target < 0):
		return False
	for num in numbers:
		if num == 0:
			return True
		remainder = target - num
		if canSum2(remainder, numbers):
			return True
	return False

##Memorization 
def canSum_memo(target, numbers, memo = {}):
	if target in memo:
		return memo[target]
	if (target == 0):
		return True
	if (target < 0):
		return False
	for num in numbers:
		if num == 0:
			memo[target] = True
			return True
		remainder = target - num
		if canSum_memo(remainder, numbers, memo):
			memo[target] = True
			return True
	memo[target] = False
	return False

print(canSum_memo(7,[3,4, 0]))
memo = {}
print(canSum_memo(7,[4,9], memo={}))
