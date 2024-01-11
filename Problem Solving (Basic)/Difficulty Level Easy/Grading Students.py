# https://www.hackerrank.com/challenges/grading

def gradingStudents(grades):
    allGrades = []
    for grade in grades:
        if grade < 38 or (grade%5) == 0:
            allGrades.append(grade)
        else:
            nextMultiple = (grade//5 + 1) * 5
            if nextMultiple - grade < 3:
                allGrades.append(nextMultiple)
            else:
                allGrades.append(grade)
    return allGrades