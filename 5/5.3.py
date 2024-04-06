#wap to find the highst 3 numbers in an dictionary

dist = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6}
dist1 = sorted(dist.values(), reverse=True) #values means the number in it the actucaly value
dist2 = sorted(dist.items(), reverse=True)  #if we want key and values together then use this one
 
hights = dist1[:3]
print("The highest three values are:", hights)


