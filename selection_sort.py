def findSmallest(arr):
	smallest = arr[0] #Stores the smallest value
	smallest_index = 0 #Stores the index of the smallest value
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr): #Sorts an array
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		print("Smallest index:\t", smallest)
		newArr.append(arr.pop(smallest))
		print(newArr)
	return newArr

print(selectionSort([5, 3, 6, 2, 10]))