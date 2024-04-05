#wap to swap value of 2 variable

def swap(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return  num1, num2

num1= int(input("Enter the value of num 1:"))
num2= int(input("Enter the value of num 2:"))
print("Before swapping")
print("Value of num 1 is :",num1)
print("Value of num 2 is :",num2)

num1, num2 = swap(num1, num2)

print("After Swaping")
print("Value of num 1 is:", num1)
print("Value of num 2 is:", num2)