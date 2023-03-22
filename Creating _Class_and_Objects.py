class Student:
    section='MCA'# class attribute
    def __init__(self,na_me,cl_ass,rool_no,a_ge,s_ex='Not Known'):
        self.name=na_me#instance attributes
        self.clAss=cl_ass
        self.rool=rool_no
        self.age=a_ge
        self.sex=s_ex
    def display(self):
        print("Name of the Student:",self.name)
        print("Class of the Student:",self.clAss)
        print("Rool of the Student:",self.rool)
        print("Age of the Student:",self.age)
        print("Gender of the Student:",self.sex)

s1=Student("Nashim Biswakarma","I",24,24) #creating Objects
s2=Student("Shreya Biswakarma","I",23,21,'Female')
print(s1.section)
s1.display()
print()
print(s2.section)
s2.display()
