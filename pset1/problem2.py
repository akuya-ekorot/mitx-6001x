"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

bob = "bob"
count = 0
index = 0

# for every letter in s
for letter in s:
    if letter == "b":  # if the letter is 'b'
        sliced = s[index:index+3]
        if sliced == "bob":  # then check if the next two characters are 'ob'
            count += 1  # if they are then add to the count
    index += 1

# once all letters are checked, print out
print("Number of times bob occurs is:", count)
