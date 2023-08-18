
def insertionSort(arr):

	
	for i in range(1, len(arr)):

		key = arr[i]

		
		i = i-1
		while i>= 0 and key < arr[i] :
				arr[i + 1] = arr[i]
				i -= 1
		arr[i + 1] = key



arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	print ("% d" % arr[i],end=" ")
