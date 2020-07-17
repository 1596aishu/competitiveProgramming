"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def partition(arr, low, high):
	i = low-1
	pivot = arr[high]
	for j in range(low,high):
		if arr[j]<=pivot:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return i+1

def quick_sort(arr,low,high):
	if low<high:
		p = partition(arr,low,high)
		quick_sort(arr, low, p-1)
		quick_sort(arr, p+1, high)

def quicksort(array):
	# Your code goes here
	# pass
	l = len(array)
	quick_sort(arr, 0, l-1)
	return arr
	
	