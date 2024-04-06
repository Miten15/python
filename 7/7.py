#wap that takes string as input and cal how many upper case letters and lower case letters 

str = input("Enter the strign:")
count_upper=0
count_lower=0
for i in str:
    if (i.isupper()):
        count_upper +=1
    else:
        count_lower +=1
    
print ("Number of Uppercase Letters=",count_upper)      
print ("Number of Lowercase Letters=",count_lower)   