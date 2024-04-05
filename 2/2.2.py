#check if number is positive or negative

def check(num):
    if  num > 0:
        return "Positive"
    elif  num < 0:
        return "Negative"
    else :
        return "Zero"

num=int(input("Enter a number:"))
obj= check(num)
print(f"The entered number {num} and the number is {obj} ")   
    
     