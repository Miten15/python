#wap to reverse a list

#list = [1,2,3,4]

#list = input("Enter the numbre for the list:")

#list.reverse()
#print(list)
#--------------------------------------------------------------------------------------------------------------

numbers = input("Enter the numbers for the list separated by spaces: ").split()

numbers = [int(num) for num in numbers]

numbers.reverse()

print(numbers)