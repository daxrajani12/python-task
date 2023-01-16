from string_compare import compare_strings

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
result = compare_strings(s1, s2)

if result == 0:
    print("Strings are equal.")
else:
    print("Strings are not equal.")