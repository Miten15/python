#find the area and the perimeter of the square

def area_of_square(side_length):
    return side_length  * side_length

def perimeter_of_square(side_length):
    return 4 * side_length

# asking for inputs
side_length = float(input("Enter length: "))

print("The area of the square is:", area_of_square(side_length))
print("The perimeter of the square is:", perimeter_of_square(side_length))
