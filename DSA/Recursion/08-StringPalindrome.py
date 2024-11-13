# Q: Check if the given String is Palindrome or not

# Solution 1: Using multiple variables.

str = "madam"
rev = ""

for i in (str):
    rev = i + rev

if str==rev:
    print("Solution 1: String is Palindrome.")
else:
    print("Solution 1: String is not Palindrome.")

# Solution 2: Using Loops.

def RevString(n):
    start = 0
    end = len(n) - 1


    while start <= end:
        if n[start] != n[end]:
            print("Solution 2: String is not Palindrome.")
            return False
        
        start += 1
        end -= 1
    
    return print("Solution 2: String is Palindrome.")

n = "Prashant"
RevString(n)

# Solution 3: Using Recursion

def RevStr(m, start, end):

    if start>=end:
        print("Solution 3: String is Palindrome")
        return
    
    if m[start] != m[end]:
        print("Solution 3: String is not Palindrome")
        return

    RevStr(m, start+1, end-1)


m = "abcba"
start = 0
end = len(m) - 1
RevStr(m, start, end)