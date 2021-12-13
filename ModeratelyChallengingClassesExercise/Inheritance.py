class person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getname(self):
        return self.__name

    def getaddress(self):
        return self.__address

    def setaddress(self, address):
        self.__address = address

    def __str__(self):
        return self.__name + " (" + self.__address + ")"

class student(person):
    def __init__(self, name, address, grades={}, courses={}, numcourses=0):
        super().__init__(name, address)
        self.__name = name
        self.__address = address
        self.__grades = grades
        self.__courses = courses
        self.__numcourses = numcourses

    def addcoursegrade(self, course, grade):
        self.__courses = course
        self.__grades = grade

    def printgrades(self):
        print(self.__courses + ': ' + self.__grades)

    def __str__(self):
        return "Student: " + self.__name + "(" + self.__address + ")"

class teacher(person):
    def __init__(self, name, address, numcourses=0, courses={}):
        super().__init__(name, address)
        self.__numccourses = numcourses
        self.courses = courses

    def addcourse(self, course):
        if course in self.courses:
            return False
        else:
            self.courses = course
            return True

    def removecourse(self, course):
        if course not in self.courses:
            return False
        else:
            delattr(Teacher, 'courses')
            return True

    def __str__(self):
        return "Teacher: " + self.__name + "(" + self.__address + ")"


# Driver Code
Person = person('Peter','Indonesia')
print(Person)
Person.setaddress('Jakarta')
print(Person)
Student = student('Peter','Indonesia')
print(Student)
Student.addcoursegrade('Maths','99')
Student.printgrades()
Teacher = teacher('Peter', 'Indonesia')
print(Teacher.addcourse('Science'))
print(Teacher.removecourse('Science'))
