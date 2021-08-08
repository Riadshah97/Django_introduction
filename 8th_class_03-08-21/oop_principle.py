class dog:
    def shout(self):
        print("dog are shouting")
class cat:
    def shout(self):
        print("cat are shouting")
class Animal(dog,cat):

    def shout(self):
        print("Animal are shoution")

animal =Animal()
print(animal.shout())



print("10000000000000000000000000")
from studentImpl import studentImpl
from accounts import Accounts
student = studentImpl("Riad", "CSE")
print(student)
print(studentImpl("jihad", "BBA"))
#print(studentImpl("Hasan", "Soft"))
student1= (studentImpl("Anas", "EEE"))

print(student.get_stu_name())
print(student1.get_stu_name())

acc = Accounts("Hasan", "Soft")
print(acc.set_stu_name("hasib"))
print(acc.set_stu_dept("Social"))
print(acc.get_stu_name())
print(acc.get_stu_dept())








