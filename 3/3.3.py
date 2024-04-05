#progam to check if the number is a palindrome or not

def is_palindrome(number):
    str_number = str(number)
    reversed_str_number = str_number[::-1]
    return str_number == reversed_str_number

number= int (input("Enter a number: "))
if is_palindrome(number):
    print("The number ", number , "is a palindrome.")
else:
     print("The number ", number , "is not a palindrome.")
 

