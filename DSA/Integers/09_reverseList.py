# Reverse a given list of numbers

a = [10, 11, 12, 13, 14]
num = len(a)


# 1. Using reverse method
a.reverse()
print(a)

# 2. Using slicing method

rev_list = a[::-1]
print(rev_list)

# 3. Reverse a list in descending order

my_list = [4,1,7,3,5,9,2]

n = len(my_list)

for i in range(n):
    for j in range(n-i-1):
        if my_list[j] < my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)

# 4. Reverse a list in ascending order

for i in range(n):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)
