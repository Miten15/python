#wap to take in number and finds the sum of digits in a number

def sum_of_digits(number):
   # return sum(int(digit) for digit in str(abs(number)))
   #return sum(int(digit) for digit in  str(abs(number)))
   return sum ( int (d) for d in str(abs((number)))) 




num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("The sum of digits in the number is:", result)
