class Subjects:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @classmethod
    def createsubject(cls, data):
        id, name = data[:-1].split(';')
        new_subject = cls(name, id)
        subjectList.append(new_subject)
        return new_subject


subjectList = []

with open('student_data/subjects.csv', "r") as subjectFile:
    line = subjectFile.readline()
    while line != "":
        if line[0] != 'i':
            Subjects.createsubject(line)
        line = subjectFile.readline()
subjectFile.close()

for subject in subjectList:
    print(subject.__dict__)
