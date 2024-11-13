# Q: Print your name N times using recursion.

def PrintName(i, n):
    if(i>n):
        return
    
    print("Prashant", i)
    PrintName(i+1, n)


PrintName(1,3)