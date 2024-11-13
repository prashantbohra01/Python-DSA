# Reverse a no. and check number is Palindrome or not

# Input = 12321
# Output = 12321

num = int(input("Enter a no."))
rev = 0 
temp = num

while num>0:
    rem = num%10
    rev = (rev*10) + rem
    num = num//10

print("Reversed no. is:", rev)

if temp == rev:
    print(f"{temp} no. is Palindrome")
else:
    print(f"{temp} != {rev} ,so it is not Palindrome")