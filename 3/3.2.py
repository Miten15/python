#wap to take in number and finds the sum of digits in a number

#def sum_of_digits(number):
   # return sum(int(digit) for digit in str(abs(number)))
   #return sum(int(digit) for digit in  str(abs(number)))
   




num = input("Enter a number: ")
sum = 0
 
for i in num:
  sum=sum + int(i)

print("The sum of digits in the number is:", sum)
