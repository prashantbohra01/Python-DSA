# Q: Given an integer N. Print the Fibonacci series up to the Nth term.


# To get the full recursion series

n = 5
num1 = 0
num2 = 1

for i in range(n+1):
    print(num1, end=" ")
    num3 = num1+num2
    num1 = num2
    num2 = num3

print()

# Solution 2: To get the Nth no. from the factorial series Using Recursion

def Fibonacci(m, n1=0, n2=1):
    if m == 0:
        return n1  # Return the first Fibonacci number
    if m == 1:
        return n2  # Return the second Fibonacci number
    
    return Fibonacci(m - 1, n2, n1 + n2)  # Recursive call

m = 5
result = Fibonacci(m)
print(f"The {m}th Fibonacci number is: {result}")

# Striver Solution

def f(s):
    if s<=1:
        return s
    
    last = f(s-1)
    slast = f(s-2)
    return last+slast

print(f(4))