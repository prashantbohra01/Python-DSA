n = 5

for i in range(n):
    for j in range(n-i):
        print(" ", end='')

    for k in range(2*(i+1)):
        if k % 2 != 0:
            print("*", end='')
        else:
            print(" ", end='')
    print()