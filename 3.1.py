#wap to reverse a give number

def reverse_number(num):
    # Convert the number to a string, reverse it, and convert it back to an integer
    reversed_num = int(str(num)[::-1])
    return reversed_num

# Test the function
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("The reversed number is:", reversed_number)
