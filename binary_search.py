def binary_search(a, item):
	low = 0
	high = len(a) - 1
	while low <= high:
		print(low,high)
		#print(a[low + high],item)
		mid = int ((low + high) / 2)
		guess = a[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], 3))