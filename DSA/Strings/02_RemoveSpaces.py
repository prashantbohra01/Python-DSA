# remove spaces from given string

# 1. Using replace function
string = "Hello Programmmers .."
white = string.replace(" ", "")
print(white)

# 2. Using loop
no_space = ""

for i in string:
    if i != " ":
        no_space += i
        print(no_space)

print(no_space)
