class Grades:
    def __init__(self, data_wystawienia, wartosc, id=None, id_przed=None, id_ucznia=None):
        self.id = id
        self.id_ucz = id_ucznia
        self.id_prz = id_przed
        self.wartosc = wartosc
        self.data = data_wystawienia

    @classmethod
    def creategrade(cls, data):
        id, wartosc, czas, id_ucz, id_przed = data[:-1].split(';')
        new_grade = cls(czas, wartosc, id, id_ucz, id_przed)
        gradeList.append(new_grade)
        return new_grade

    def srednia(self):
        pass

    def srednia_z_przedmiotow(self):
        pass


gradeList = []

with open('student_data/grades.csv', "r") as gradeFile:
    line = gradeFile.readline()
    while line != "":
        print(line, end='')
        if line[0] != 'i':

            Grades.creategrade(line)
        line = gradeFile.readline()
gradeFile.close()

for grade in gradeList:
    print(grade.__dict__)
