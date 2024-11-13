# Reverse the entire sentence

string = "India is country My"

string = string.split()
length = len(string)

updated_str = ""

for i in range(length):
    updated_str =  string[i] + " " +updated_str
    
print(updated_str)