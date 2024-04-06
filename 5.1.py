#find the repated number in tuple

tu=(1,1,1,1,2,2,3,3,5,5,4)
dup = []

for num in tu:
        if tu.count(num) > 1:
            dup.append(num)
print("The repeated elements are : ",end='')
for num in dup:
    print(num, end=" ")
