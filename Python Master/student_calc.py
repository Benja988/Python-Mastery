def calculate_total(marks):
    """Return the total marks from a list of marks."""
    return sum(marks)

def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
def student_report(name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    return f"Name: {name}\nTotal: {total}\nAverage: {average}\nGrade: {grade}"