#wap to find the area and the circumference of  a circle

import math

r = float(input("Enter the radius of the crile:"))
area=math.pi * r**2 #'**' is used to make the number ^2.

circumference=2* math.pi * r
print ("The area of the circle is", area)
print ("The circumference of the circle is", circumference)
