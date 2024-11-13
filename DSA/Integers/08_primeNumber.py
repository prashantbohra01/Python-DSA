# Prime number
# Prime number is a number that is greater than 1 and divided by 1 or itself only

from cmath import log


num = int(input("Enter a no: "))
count = 0 

if num <= 1:
    print("No. is not a Prime number")

for i in range(1, num + 1):
    if num%i==0:
        count += 1    

if count == 2:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")
    





