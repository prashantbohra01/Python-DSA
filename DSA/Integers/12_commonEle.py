# Finding common elements in arrays

# arr1 = [4,2,3,1,6], arr2 = [6,7,8,4]
# output = 6,4

arr1 = [4,2,3,1,6,7]
arr2 = [6,7,8,4]
common = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            common.append(arr1[i])

print(common)