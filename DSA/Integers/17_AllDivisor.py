# A divisor of an integer N is a positive integer that divides N without leaving a remainder. 
# In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

n = 6
divisor = []

for i in range(1,n+1):
    if n%i==0:
        divisor.append(i)

print(f"All the Divisor of number {n} are {divisor}")