""" class Teacher:
    def __init__(self, name):
        self.teacherName = name
        self.students = []
    def  entry_student( self, studentObj ):
        self.students.append(studentObj)
    
class Student:
    def __init__(self, name) -> None:
        self.studentName = name

    def enter_in_a_teacher( self, teacherObj ):
        teacherObj.students.append( self )

    def __repr__(self) -> str:
        return f"Student({self.studentName})"

rahim_mia = Teacher('Rahim Mia')
ms_rahima = Teacher('Ms Rahima')
solaiman_sir = Teacher('Solaiman mia')

student = Student('karim')
student.enter_in_a_teacher( rahim_mia )
student.enter_in_a_teacher( ms_rahima )

print(rahim_mia.students)
print(solaiman_sir.students)
print(ms_rahima.students)
 """

# ********* One more Duck Type Example *******


class School:
    def __init__( self, name ) -> None:
        self.schoolName = name

    def say_hello( self ):
        print('Hello From School')

class Teacher:
    def __init__(self, name):
        self.teacherName = name
    
    def say_hello( self ):
        print(f'Hello From Teacher')

class Student:
    def __init__(self, name, obj ) -> None:
        self.studentName = name
        obj.say_hello()

school = School('Trust School')
teacher = Teacher('Solaiman Sir')

student = Student('Rakib', teacher )