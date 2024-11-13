# Recursion is when a function calls itself indefinitely until a specified condition is met.

def recursion():
    print(1)

    recursion()

# recursion()



# Stack Overflow: A stack overflow happens when a function keeps calling itself too many times without stopping, 
# which causes the computer to run out of memory for those calls.

# A base condition (or base case) is a condition in recursion that stops the function from calling itself endlessly. 
# Without it, you would run into a stack overflow. The base condition tells the function when to stop.

#count = 0

def rec(count=0):
    if count==3:   # Base Condition
        print("Taking exit from recursion")
        return
    
    print(count)
    count += 1
    rec(count)

rec()