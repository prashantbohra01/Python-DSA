def remove_element(arr, num):
    result = [] # Create an empty list to store elements that are not equal to num
    
    for element in arr: # Iterate through each element in the original list
        
        if element != num: # If the element is not equal to the number to remove, add it to the result list
            result.append(element)
    
    return result

# Test the function
arr = [1, 2, 3, 4, 2, 5, 2]
num_to_remove = 2
new_arr = remove_element(arr, num_to_remove)

print("Original list:", arr)
print("Number to remove:", num_to_remove)
print("New list:", new_arr)
