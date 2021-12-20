class Student:
    def __init__(self, nexp, subject, score):
        self.nexp = nexp
        self.subject = subject
        self.score = score

    def has_passed(self, score_to_pass):
        return self.score >= score_to_pass

    def __str__(self):
        return str(self.nexp) + " " + self.subject + " " + str(self.score)



student_1 = Student(1, "PF", 7.5) #1
student_2 = Student(2, "PF", 9.25) #2
student_3 = Student(3, "PF", 4.99) #3

list_students = []
list_students.append(student_1)
list_students.append(student_2)
list_students.append(student_3)

for student in list_students:
    print(student)