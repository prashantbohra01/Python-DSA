n = 5

for i in range(n):
    for j in range(n-i):
        print("*", end='')
    
    print()


for i in range(1, n+1):
    for j in range(1, n-i+2):
        print(j , end='')
    
    print()