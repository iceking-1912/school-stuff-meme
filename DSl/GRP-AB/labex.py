# N = int(input("No. of Natural no.: "))
# num_list = []
# for i in range(0, N):
#     num = int(input("Enter number: "))
#     num_list.append(num)
# sumnum = 0
# for i in range(0, N):
#     sum += num_list[i]
#
# avg = sumnum / N
#
# print(num_list)
# print(avg)
# print(max(num_list))
# print(min(num_list))
# if N != len(num_list):
#     print("No. of Student abesnt-")
#     print(N - len(num_list))
# else:
#     print("No Student ws absent for FDS exam")
#
# for i in num_list:
#     for j in num_list:
#         c = 1
#         if i == j:
#             c += 1
#         else:
#             pass
# print(c)

# 2) Write a Python program to compute following operations on String:
# a) To display word with the longest length
# b) To determines the frequency of occurrence of particular character in the string
# c) To check whether given string is palindrome or not
# d) To display index of first appearance of the substring
# e) To count the occurrences of each word in a given string.
# string = "It is decided that weekly greetings are to be furnished to wish"


string = "It is decided that weekly greetings are to be furnished to wish"

print("Given Sttring is", f'"{string}"')
split_string = string.split(" ")

# a) To display word with the longest length
len_word_spit_string = []
for i in split_string:
    word_len = len(i)
    len_word_spit_string.append(word_len)
print("A)The word with the longest length is-", end=" ")
print(split_string[len_word_spit_string.index(max(len_word_spit_string))])

# b) To determines the frequency of occurrence of particular character in the string
combine_list = ""
for i in split_string:
    combine_list += i
char_freq = {}
for char in combine_list:
    char_freq[combine_list.count(char)] = char
print(
    "B)The frequency of occurrence of particular character in the string is-", end=" "
)
print(char_freq.get(max(char_freq)))

# c) To check whether given string is palindrome or not
r_string = string[::-1]
if string == r_string:
    print("This String is a Palindrome")
else:
    print("This is Not a Palindrome")

# d) To display index of first appearance of the substring
sub_string = "to"
print("D)The Sub-String is-", f'"{sub_string}"')
c = string.find(sub_string, 0, len(string))
if c == -1:
    print("This Sub-String does not Exist in String")
elif c != 1:
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
