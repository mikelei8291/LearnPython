class Lesson():
    def __init__(self, title, time, lab):
        super(Lesson, self).__init__()
        self.title = ""
        self.time = 0
        self.lab = False

class Assessment():
    def __init__(self, title, maxMark):
        super(Assessment, self).__init__()
        self.title = ""
        self.maxMark = 0

class Course():
    def __init__(self, t, m):
        super(Course, self).__init__()
        self.__title = t
        self.__studentsNum = m
        self.__lessonNum = 0
        self.__lessonContent = []
        self.__assesment = Assessment

    def addLesson(self, t, d, r):
        self.__lessonNum += 1
        self.__lessonContent.append(Lesson(t, d, r))

    def addAssesment(self, t, m):
        self.__assesment = Assessment(t, m)

    def showCourseInfo(self):
        print("{0}\nMaximum number: \n{1}".format(self.__title, self.__studentsNum))
        for i in range(self.__lessonNum):
            print(self.__lessonContent[i].showCourseInfo())

def __main__():
    myCourse = Course("Computer Science", 10)
    myCourse.addAssesment("Programming", 100)

    myCourse.addLesson("Problem Solving", 60, False)
    myCourse.addLesson("Programming", 120, True)
    myCourse.addLesson("Theory", 60, False)

    myCourse.showCourseInfo()
