# Q: Given a no. N, find out the sum of the first N natural numbers.

# Solution 1: Using Loop

n= 5
sum = 0

for i in range(1, n+1):
    sum = sum + i   

print(sum)

# Solution 2: Using Formula 


def SumOfN(n):
    sum = n * (n + 1) / 2
    print((sum))

SumOfN(5)
SumOfN(6)

# Solution 3: Using Recursion

sum = 0
def PrintSum(n, sum):
    if n<1:
        print(sum)
        return
    
    PrintSum(n-1, sum+n)

PrintSum(5, sum)