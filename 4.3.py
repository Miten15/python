#find common number in the list

#list =  [1,2,3,4,5,1,1]
#list2 =  [1,2,3,1,1]
#for num in list1:
 #   if num in list2:
  #      common_numbers.append(num)

#print("Common numbers in the lists:", common_numbers)

#--------------------------------------------------------------------------------------------------------------


list1 = input("Enter the value with spacing",).split()
list2 = input("Enter the value with spacing",).split()
common_numbers = []
for num in list1:
    if num in list2:
        common_numbers.append(num)

print("Common numbers in the lists:", common_numbers)