# Armstrong no. is a number that is equal to the sum of cubes of its digits.


# for example we are taking an input 153 , which is (1*1*1) + (5*5*5) + (3*3*3) = 153

n = int(input("Enter a no. "))
sum = 0
order = len(str(n))
copy_n = n

while(n > 0):
    digit = n%10 
    sum += digit ** order
    n = n//10

if (sum == copy_n):
    print(copy_n, "is an Armstrong no.")
else:
    print(copy_n, "not an Armstrong no.")