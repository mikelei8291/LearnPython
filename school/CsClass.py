class csClass():
    def __init__(self):
        super(csClass, self).__init__()
        self.classroom = ""
        self.studentName = []
        self.teacherName = ""
        self.time = ""
        self.chapter = 0


classLuLu = csClass()
classLuLu.studentName = ["John", "Joy", "Steve"]
print(classLuLu.studentName[2])
csGroup = [csClass for i in range(5)]
csGroup[2].chapter = 25
print(csGroup[2].chapter, csGroup[0].chapter)
