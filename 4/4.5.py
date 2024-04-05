#wap to find even number in the list

#list = input("Enter the number  of elements you want in your list:",).split()
#num_list = int(list)


list=  [1,2,3,4,5]
nim = []
for num in list:
    if num % 2 == 0:
        nim.append(num)

print(f"The Even numbers are {nim}")

