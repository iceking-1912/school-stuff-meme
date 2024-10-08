#labex-2-code
string = "It is decided that weekly greetings are to be furnished to wish"
print("Given String is", f'"{string}"')
split_string = string.split(" ")

# a) To display word with the longest length
len_word_spit_string = []
for i in split_string:
    word_len = len(i)
    len_word_spit_string.append(word_len)
print("A)The word with the longest length is-", end=" ")
print(split_string[len_word_spit_string.index(max(len_word_spit_string))])

# b) To determine the frequency of occurrence of each character in the string
combine_list = ""
for i in split_string:
    combine_list += i

char_freq = {}
for char in combine_list:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

particular_char = input("Enter the character to find its frequency: ")

if particular_char in char_freq:
    print(f"B) The frequency of occurrence of '{particular_char}' in the string is {char_freq[particular_char]}")
else:
    print(f"B) The character '{particular_char}' is not present in the string")

# c) To check whether given string is palindrome or not
r_string = string[::-1]
if string == r_string:
    print("C) This String is a Palindrome")
else:
    print("C) This is Not a Palindrome")

# d) To display index of first appearance of the substring
sub_string = "to"
print("D)The Sub-String is-", f'"{sub_string}"')
c = string.find(sub_string, 0, len(string))
if (c == -1):
    print("This Sub-String does not Exist in String")
elif (c != 1):
    print("This Sub-String Exist in String at Index-", c)
else:
    print("This Sub-String does not Exist in String")

# e) To count the occurrences of each word in a given string.
word_freq = {}
for i in split_string:
    word_freq[i] = split_string.count(i)
print("e)The occurrences of each word in a given string-")
for i in word_freq:
    print(i, end=" : ")
    print(word_freq.get(i))

#Output:
# Given String is "It is decided that weekly greetings are to be furnished to wish"
# A)The word with the longest length is- greetings
# Enter the character to find its frequency: i
# B) The frequency of occurrence of 'i' in the string is 5
# C) This is Not a Palindrome
# D)The Sub-String is- "to"
# This Sub-String Exist in String at Index- 40
# e)The occurrences of each word in a given string-
# It : 1
# is : 1
# decided : 1
# that : 1
# weekly : 1
# greetings : 1
# are : 1
# to : 2
# be : 1
# furnished : 1
# wish : 1