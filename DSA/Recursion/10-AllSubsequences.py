# Print all subsequences: A contigous/non contigous sequences, which follow the order
# Example : arr = [3,1,2]
# Subsequences of arr = {}, 3, 1, 2, 3 1, 1 2, 3 2, 3 1 2  == 8

def PrintF(index, current, arr, n):
    if index==n:
        print(current)
        return
    
    PrintF(index+1, current, arr, n)
    current.append(arr[index])

    PrintF(index+1, current, arr, n)
    current.pop()


arr= [3,1,2]
n = 3
PrintF(0, [], arr, n)    
