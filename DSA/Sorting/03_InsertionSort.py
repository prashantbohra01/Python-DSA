# Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

# Example:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: 
# After sorting the array is: 9,13,20,24,46,52

# Insertion Sort is a simple sorting algorithm that builds the final sorted list one item at a time. It works by taking each element from the unsorted part of the list 
# and inserting it into the correct position in the sorted part of the list.


arr = [13,46,24,52,20,9]
n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(arr)