class student:
    def __init__(self,__name,__roll):
        self.__name = __name
        self.__roll = __roll
    def setName(self,__name):
        self.__name = __name
    def getName(self,):
        return self.__name
    def setRoll(self,__roll):
        self.__roll = __roll
    def getRoll(self,):
        return self.__roll
student = student("Thaseen",92)
print(student.getName())
print(student.getRoll())