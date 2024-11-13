# Write a program to make a dynamic list.  


#Dynamic list
a = []
size = int(input("Enter Size of list: "))

for i in range(size):
    val= int(input("Enter Value: "))
    a.append(val)
    
print("Original list = ", a)

key = int(input("Enter a value to delete: "))
flag = 0
for i in range(size):
    if a[i] == key:
        flag = 1
        pos = i
        break

if flag == 0:
    print("Element not found")
else:
    for i in range(pos, size-1):
        a[i]= a[i+1]

a.pop(size-1)
print("list after deletion = ", a)

