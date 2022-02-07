# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
# If you have time, come back to this problem after you've had a break and cleared your head.

# s = "azcbobobegghbegghakl"

index = 0
lists = []

for letter in s:
    substring = s[index:len(s)]
    subindex = 0
    sublength = len(substring)

    # print(substring)
    # print("Starting to check from", letter,
    #       "at index", index, "out of", len(s) - 1)

    array = []
    array.append(letter)

    for l in substring:

        if subindex - (sublength - 1) != 0:
            # print("Checking", l, "and", substring[subindex - (sublength - 1)])

            if l <= substring[subindex - (sublength - 1)]:
                # print("Test passed...")
                array.append(substring[subindex - (sublength - 1)])
            else:
                # print("Test failed...")
                break

            subindex += 1
    lists.append(array)
    # print(array)
    index += 1


lists_length = []

for list in lists:
    lists_length.append(len(list))

# print(lists_length)
# print(max(lists_length))

longest_array = lists[lists_length.index(max(lists_length))]
longest = "".join(longest_array)

print(" Longest substring in alphabetical order is:", longest)