#fact of a number
import math

def fact(num):
    return math.factorial(num)

num = int(input(f"Enter the number: "))
print(f"\nThe factorial of  {num} is : {fact(num)}")