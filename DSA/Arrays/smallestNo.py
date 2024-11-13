# Find the smallest no. in an Array

a = [21, 24, 12, 16, 6, 19]
n = len(a)
smallest = a[0]   # assuming

# 1. Using sorting the Arrayt

for i in range (n):
    for j in range(n-i-1):
       if a[j]>a[j+1]:
           a[j], a[j+1] = a[j+1], a[j]

print("The smallest no. is" ,a[0])

# 2. Using loop and if or using brute force

for i in a:
    if i < smallest:
        smallest = i

print("Smallest no.",smallest)