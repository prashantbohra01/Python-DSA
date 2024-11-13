# Find majority element in an array (an element that appears more than n/2 times, where n is the size of array)

arr = [1,2,3,2,2,4,2,5,2]
n = len(arr)

majority_element = None

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i]==arr[j]:
            count += 1
        
    
    if count > n//2:
        majority_element = arr[i]
        break
        
print(majority_element)