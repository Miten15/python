# program to sum all the list

#lst =  [1,2,3,4,5]
#lst = input("Enter the values separated by spaces: ").split()
#for i in range (len(newlst)):
 #   sum = sum+int(newlst[i])
    
#print("The sum of the list is: ", newlst)




lst = input("enter the values")

newlst = list(lst)


list_sum = 0

for num in newlst:
    list_sum += int(num)

print("The sum of the list is:", list_sum)
