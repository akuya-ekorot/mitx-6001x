"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
your program should print: Number of vowels: 5
"""

vowels = "aeiou"
count = 0
# loop through all the letters in the string s
for letter in s:  # for every letter,
    if letter in vowels:  # check whether it's a vowel
        count += 1  # if it's a vowel, increase the count

# once all letters in the strings are checked, print out the total count
print("Number of vowels:", count)
