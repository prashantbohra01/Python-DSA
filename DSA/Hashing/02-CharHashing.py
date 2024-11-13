# Character Hashing:

# Given the string: “abcdabefc” we are given some queries: [a, c, z]. For each query, we need to find out how many times the character appears in the string. 
# For example, if the query is ‘a’ our answer would be 2, and if the query is ‘z’ the answer will be 0. 
import sys

# SOLUTION 1:

s = "ababcadefc"

hash_arr = [0]*26

for i in s:
    hash_arr[ord(i) - ord('a')] += 1

q = int(input("Enter the number of queries: "))
for _ in range(q):
    # Take character input for each query
    char = input("Enter the character to find: ")
    # Fetch and print the frequency
    print(f"{char} appears {hash_arr[ord(char) - ord('a')]} times.")



# SOLUTION 2: Using Dictionary in python
hash_map = {}

for i in s:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

q = int(input("Enter the number of queries: "))
for _ in range(q):
    # Take character input for each query
    char = input("Enter the character to find: ")
    # Fetch and print the frequency
    print(f"{char} appears {hash_arr[ord(char) - ord('a')]} times.")