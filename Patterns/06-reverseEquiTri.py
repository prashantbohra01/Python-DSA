n = 5

for i in range(n):
    for j in range(i+1):
        print(" ", end='')
    
    for k in range(2*(n-i)-1):
        print("*", end='')

    print()