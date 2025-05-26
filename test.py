class StudentRecord:
    def __init__(self, StudentName, RollNumber, TotalMarks):
     self.StudentName = StudentName
     self.RollNumber = RollNumber
     self.TotalMarks = TotalMarks

    def DisplayDetails(self):
        print(f"Name: {self.StudentName}")
        print(f"Roll No: {self.RollNumber}")
        print(f"Total Marks: {self.TotalMarks}")


StudentOne = StudentRecord("Yash", 101, 450)
StudentOne.DisplayDetails()
