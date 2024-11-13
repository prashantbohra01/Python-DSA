a = 100
b = 200

# 1. Swapping using three variables

temp = a
a = b
b = temp

print("After swapping, a =", a , "and b =", b)

# 2. Using two Variables only

a = a + b
b = a - b
a = a - b
print("After swapping, a =", a , "and b =", b)

# 3. Swapping using XOR

a = a^b
b = a^b
a = a^b
print("After swapping, a =", a , "and b =", b)
