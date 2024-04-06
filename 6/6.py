#wap to perform intersection set , union of set , set diff ,symmetric diff and clear a set

set1 = {1, 2, 3, 4, 5,75}
set2 = {56, 8, 75}

intersection_set = set1.intersection(set2)  # performing intersection operation on two sets
print("Intersection Set:", intersection_set) #to check common number in 2 sets

#union
union_set = set1.union(set2)   #performing union operation on two sets
print("Union Set:", union_set) # combines both sets tograther 

#difference
diff = set1.difference(set2)     #finds the difference between two sets
print("diff set=", diff)

#symmetric diff
symmetric = set1.symmetric_difference(set2)
print("Symmetric Diff : ", symmetric)    #gives numbers which are not present in both sets

#clearing a set
c = set1.clear()
print("hahahha can u see it??",set1)