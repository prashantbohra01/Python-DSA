# Hashing is a process where we take a piece of data (like a word or number) and use a special function (called a hash function) to turn it into a unique number. 
# This number helps us store the data in a table (called a hash table) so we can find it quickly later.
# It is nothing but combination of steps, prestoring abd fetching.


# SOLUTION 1: 
def count_occurrences():
    # Input size of the array
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))

    # Precompute occurrences using a hash array (list)
    hash_array = [0] * 13  # List of size 13 to count occurrences
    for num in arr:
        hash_array[num] += 1  # Increment the count at index `num`

    # Input number of queries
    q = int(input("Enter the number of queries: "))
    for _ in range(q):
        number = int(input())
        # Fetching occurrences
        print(hash_array[number])  # Output the count of `number`

#count_occurrences()



# If you don't provide a fixed size for the hash_array (which is 13 in this case) and still want to apply a hashing approach, 
# you can dynamically create the hash map based on the input values. In Python, using a dictionary (which works as a hash map) is a more flexible and common approach. 
# This way, you don't need to predetermine the size of the hash array because the dictionary can grow dynamically as you add new keys (elements of the array).


# SOLUTION 2:
arr = [1,3,2,1,3]
hash_map = {}

for i in arr:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

q = int(input("Enter the number of queries: "))

for _ in range(q):
    number = int(input())
    # Fetching occurrences
    print(f"{number} appears {hash_map.get(number, 0)} times.")  # Defaults to 0 if the number is not found


