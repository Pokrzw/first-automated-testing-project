class Student:
    student_id = 0

    def __init__(self, first, last, id=None, uwagi=""):
        self.first = first
        self.last = last
        self.id = '{}_ucz'.format(Student.student_id)  # tutaj poprawic dac ifa
        self.uwagi = uwagi
        Student.student_id += 1

    @classmethod
    def createStudent(cls, data):
        id, first, last, uwagi = data[:-1].split(';')
        #print("Created student: {} {}.".format(first, last))
        new_student = cls(first, last, id, uwagi)
        studentList.append(new_student)
        return new_student

    def delStudent(self):
        for student in studentList:
            if student.id == self.id:
                studentList.remove(student)

    def changeName(self, newF="", newL=""):
        if newF != "":
            self.first = newF
        if newL != "":
            self.last = newL


studentList = []

with open('student_data/students.csv', "r") as studentFile:
    line = studentFile.readline()
    while line != "":
        if line[0] != 'i':
            Student.createStudent(line)
        line = studentFile.readline()
studentFile.close()

for student in studentList:
    print(student.__dict__)
