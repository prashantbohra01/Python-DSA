# Count digits in an integer number
# input = 29845315
# output = 8

num = 29845315
count = 0

while(num != 0):
    num = num//10
    count = count + 1

print(count)