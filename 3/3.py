#print even number from 1 - 100

def  print_even(num):
    if num % 2 == 0:
        return num
    
for i in range (1, 101):
    result = print_even(i)
    if result != None:
        print(result)