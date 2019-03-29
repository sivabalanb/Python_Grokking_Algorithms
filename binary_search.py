def binary_search(a, item):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)
		guess = a[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

print(binary_search([1,2,3,4,5,6,7], 4))