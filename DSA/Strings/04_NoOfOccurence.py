# Counting no. of occurences of given word in a string

string = "Python is a programming language. Python is widely used in software testing. Python"
word = "python"

string = string.lower().split()
length = len(string)
count = 0

for i in range(length):
    if string[i]==word:
        count = count+1

print(count)
