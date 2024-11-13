# Fibbonacci series 
# In fibonacci series, next no. is the sum of previous two numbers

num1 = 0
num2 = 1
num = int(input("Enter a no. "))

for i in range (num):
    print(num1, " ")
    num3 = num1 + num2
    num1 = num2
    num2 = num3
