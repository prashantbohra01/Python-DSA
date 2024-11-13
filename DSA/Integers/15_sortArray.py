# Sort an array without using prebuilt functions
# Bubble sort algorithm

arr = [10, 5, 20, 63, 12, 57, 88, 60]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


# find the third largest element in the list
print(arr[n-3])

