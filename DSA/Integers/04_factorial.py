# Factorial Number
# Factorial of n is the product of all positive descending integers.

num = int(input("Enter a no. to get the factorial:"))
fact = 1

for i in range (1, num+1):
    fact = fact * i

print(f"Factorial of {num} is", fact)