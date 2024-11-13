# Bubble Sort Algorithm
# Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

# Example 1:
# Input: N = 6, arr = [13,46,24,52,20,9]
# Output: 9,13,20,24,46,52
# Explanation: After sorting we get 9,13,20,24,46,52


# ** Bubble Sort pushes the maximum to the last by adjacent swaps **

arr = [13,46,24,52,20,]
n = len(arr)

for i in range(n-1):
    swapped = False  # To check if any swaps happened in this pass
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] # Swap the elements
            swapped = True  # Mark that a swap happened

    if not swapped:  # If no swaps happened in this pass, the array is already sorted
        break    

    print("runs")

print(arr)

