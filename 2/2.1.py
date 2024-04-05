#wap to check the largest number among 3 number

def max_number(a, b, c):
    return max(a, b, c)

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print("The largest number is:", max_number(num1, num2, num3))

