# Q: Print 1 to N without using loops

def PrintNos(n):
    if n == 0:
        return
    
    PrintNos(n-1)
    print(n, end=' ')

PrintNos(10)


print()

# Q: Print N to 1 using recursion

def PrintN(n):
    if n == 0:
        return
    
    print(n, end=' ')
    PrintN(n-1)

PrintN(10)