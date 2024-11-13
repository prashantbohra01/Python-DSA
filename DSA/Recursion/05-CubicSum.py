# Q: Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.
# Example: Input: n=5
#          Output: 225
# Explanation: 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225


sum = 0
def PrintSum(n, sum):
    if n<1:
        print(sum)
        return
    
    PrintSum(n-1, sum+(n**3))

PrintSum(5, sum)