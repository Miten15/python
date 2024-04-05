#wap to take input of 5 subject and display the grade

def grade(marks):
    avg = sum(marks) / len(marks)

    if avg >= 90:
        return "Grade A+"
    elif avg >= 85:
        return "Grade A"
    elif avg >= 80:
        return "Grade B"
    elif avg >= 70:
        return "Grade C"
    elif avg >= 60:
        return "Grade D"
    else:
        return "Fail"
    
marks = []
for i in range(5):
    mark = float(input("Enter the marks of subject {}: ".format(i+1)))
    while mark < 0 or mark > 100:
        print("Invalid Marks. Please Enter Again")
        mark = float(input("Enter the marks of subject {}: ".format(i+1)))
    marks.append(mark)
    
print(grade(marks))


    