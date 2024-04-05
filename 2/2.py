#wap to check if the number is even or odd

def check(num):
    if num % 2 == 0:
        return "The number is Even"
    else:
        return "The Number is Odd"

#taking user input
num = int(input("Enter a number :"))
print(check(num))