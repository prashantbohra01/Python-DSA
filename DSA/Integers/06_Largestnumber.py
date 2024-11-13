# Largest Number from 3 number given list

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

# 1. Using If-else condition

if num1>=num2 and num1>=num3:
    print(num1, "is the largest number.")
elif num2>=num1 and num2>=num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# 2. Using Max() function

largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")
