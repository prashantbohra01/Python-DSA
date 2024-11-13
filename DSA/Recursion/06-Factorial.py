# Factorial of N
# Example : input = 5
#           output = 120
# Explanation : 5*4*3*2*1 = 120


# Solution 1: Using Loops

fact = 1
n = 5
temp = n
for i in range(1, n+1):
    fact = fact*i

print(fact)

# Solution 2: Using Recursion


def Factorial(n, fac):
    if n<1:
        print(f"Factorial of {temp} is {fac}")
        return
    
    Factorial(n-1, fac*n)

fac = 1
Factorial(5, fac)