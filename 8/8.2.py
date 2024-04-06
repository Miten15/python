#takes an string from user and check how many upper case and lowwer case char are there


def count_chars(s):
    lower = 0
    upper = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("Number of Lowercase Letters:", lower)
    print("Number of Uppercase Letters:", upper)

str_input = input("Enter a string: ")
count_chars(str_input)

