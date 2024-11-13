# reverse a string
# input = hello
# output = olleh

string = "hello"

# 1. Using Slicing

reversed_string = string[::-1]
# print(reversed_string)

# 2. using Loop

n = "hello"
rev = ""

for char in n:
    rev = char + rev
    print(rev)

print(rev)