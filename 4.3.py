#find common number in the list

list =  [1,2,3,4,5,1,1]
list2 =  [1,2,3,1,1]
common_numbers = []
for num in list:
    if num in list2:
        common_numbers.append(num)

print("Common numbers in the lists:", common_numbers)