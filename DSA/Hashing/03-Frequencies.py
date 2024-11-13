# Q: Find the highest/Lowest frequency element

# Example: arr = [10, 5, 10, 15, 10 , 5]
# Output: 10 15
# Explanation: The frequency of 10 is 3 i.e the highest and the frequency of 15 is 1 i.e the lowest.

arr = [10,5,10,15,10,5]
hash_arr = {}
max_freq = -1   # Initialize max frequency
min_freq = float('inf')  # Initialize min frequency

for i in arr:
    if i in hash_arr:
        hash_arr[i] += 1
    else:
        hash_arr[i] = 1
    # Update max frequency
    if hash_arr[i] > max_freq:
        max_freq = hash_arr[i]

    # Update min frequency
    if hash_arr[i] < min_freq:
        min_freq = hash_arr[i]


# Step 2: Find elements with highest and lowest frequency
max_freq_elements = []
min_freq_elements = []

for key, value in hash_arr.items():
    if value == max_freq:
        max_freq_elements.append(key)
    if value == min_freq:
        min_freq_elements.append(key)

# Step 3: Output the results directly
print("Elements with highest frequency:", max_freq, "=>", max_freq_elements)
print("Elements with lowest frequency:", min_freq,"=>", min_freq_elements)