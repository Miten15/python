#wap a python function that takes a number as a param and check if its prim or not
import math

def is_prime(num):

    if num < 2:
        return "is not a prime number"
    
    for i in range(2, int(math.sqrt(num)) ):
        if num % i == 0:
            return "Not a prime number"
    
    return "is a prime number"

num = int(input("Enter a number: "))
print(num, "",is_prime(num))
