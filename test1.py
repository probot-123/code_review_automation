def calculateTotalMarks(subjectOne, subjectTwo, subjectThree):
    totalMarks = subjectOne + subjectTwo + subjectThree
    return totalMarks

studentName = "Yash"
subjectOneMarks = 85
subjectTwoMarks = 90
subjectThreeMarks = 88

finalScore = calculateTotalMarks(subjectOneMarks, subjectTwoMarks, subjectThreeMarks)

print(f"Student: {studentName}")
print(f"Total Marks: {finalScore}")
