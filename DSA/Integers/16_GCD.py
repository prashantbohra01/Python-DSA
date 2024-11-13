# Q: GCD - Greatest common divisor or HCF- Highest common factor

n1= 12
n2= 9

gcd = 1

for i in range(1, min(n1,n2)):
    if(n1%i==0 and n2%i==0):
        gcd = i

print(gcd)


# Q: Armstrong Number.

n = 1634
sum = 0
temp = n

degree = len(str(n))

while n>0:
    rem = n%10
    sum = sum + rem**degree
    n = n//10

if temp==sum:
    print(f"{temp}, It is an Armstrong no.")
else:
    print(f"{temp}, It is not an Armstrong no.")