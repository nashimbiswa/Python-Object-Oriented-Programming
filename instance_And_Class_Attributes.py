class Student:
    section='MCA'# class attribute
    sexx='Female'
    def __init__(self):
        self.sexx='f'
    def changeSex(self):
        self.sexx=Student.sexx #use self to use instance attributes


s1=Student()
print(s1.sexx)
s1.changeSex()
print(s1.sexx)