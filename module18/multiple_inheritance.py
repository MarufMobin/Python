class School:
    def __init__(self,name):
        self.schoolName = name
    
    def say_hello( self ):
        print(f'Hello i am {self.schoolName}')

    def __repr__(self):
        return f"School({self.schoolName})"

class Teacher:
    def __init__(self, name) -> None:
        self.teacherName = name
    
    def say_hello( self ):
        print(f'Hello i am {self.teacherName}')

    def __repr__(self) -> str:
        return f"Teacher({self.teacherName})"
    
class Student( Teacher, School ):

    def __init__(self, name, teacherName, SchoolName ) -> None:
        self.studentName = name

        Teacher.__init__( self, teacherName )
        School.__init__( self, SchoolName )
        # super().__init__( teacherName ) # there Only folow Order which one are forward and which one are backword ## jodi 2 ta inherit hoye thake tile must Name diye diye amk use krte hbe super --> diye kaj krbe na

    def say_hello( self ):
        print(f'Hello i am {self.studentName}')

    
    def __repr__(self) -> str:
        return f"Student({self.studentName})"


student = Student('Maruf', 'Ms. Kanij Fatema', 'Trust School')
print(student.teacherName)
print(student.schoolName)
student.say_hello()
#  Ai khane jodi say_hello tar nijer i method thake tobe take call krbe notuba tar parent ar argument ar order wise ta call kre then kaj krbe ai kaj takei bla hoi (method resolution order)