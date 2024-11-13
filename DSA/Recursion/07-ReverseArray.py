# Q: Reverse a given Array

# Input: [5,4,3,2,1]
# Output: [1,2,3,4,5]

# Solution 1: Using an extra Array (Using loops)

n = [5,4,3,2,1]
arr = []

for i in range(1, len(n)+1):
    arr = arr + [i]

print("Solution 1:", arr)

# Solution 2: Space-Optimized iterative method (Using Loops)

def RevArray(ar):
    start = 0
    end = len(ar) - 1

    while start<=end:
        ar[start], ar[end] = ar[end], ar[start]
        start += 1
        end -= 1

    print("Solution 2:",ar)

ar = [5,4,3,2,1]
RevArray(ar)

# Solution 3: Using Recursion

def ReverseArray(array, start, end):

    if start >= end:
        print("Solution 3:", array)
        return

    array[start], array[end] = array[end], array[start] 
    ReverseArray(array, start+1, end-1)

array = [5,4,3,2,1]
start =  0
end = len(array) - 1
ReverseArray(array, start, end)