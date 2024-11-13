# Sum of digits

# input = 987
# output = 24 (9+8+7)

n = 987
sum = 0

while(n!=0):
    sum = sum + n%10
    n = n//10

print(sum)