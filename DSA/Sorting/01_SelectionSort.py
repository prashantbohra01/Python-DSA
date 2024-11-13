# Selection Sort Algorithm
# Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.
# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

arr = [13,46,24,52,20,9]
n = len(arr)

for i in range(n-1):
    min_idx = i
    
    for j in range(i+1,n):
        if arr[j]<arr[min_idx]:
            min_idx = j
    
    arr[i],arr[min_idx] = arr[min_idx], arr[i]
    print(arr)
            
    
print("Final Selection sort array list:-",arr)