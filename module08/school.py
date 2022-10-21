class Student:
    def __init__( self, name, age, id ):
        self.name = name
        self.age = age
        self.id = id
    
class Course:
    def __init__(self, name, teacher ):
        self.name = name
        self.teacher = teacher
    
class Teacher:
    def __init__( self, name, course ):
        self.name = name
        self.course = course

class School:
    def __init__(self, name, teachers, courses , students ):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students
    def get_students( self ):
        for student in self.students:
            print(f'Student Name : {student.name} ->  Student age : {student.age} -> Student id : {student.id} ')

school_name = 'Phitron'

ds_course = Course('Data Stracture', 'Akib Jamman')
teacher_1 = Teacher('Akib Jamman', ds_course )

algo_course = Course('algorithm', 'Shihaf adnan')
teacher_2 = Teacher('Shihaf adnan', algo_course )

py_course = Course('Python', 'Jhanker Mahbub')
teacher_3 = Teacher('Jhanker Mahbub', py_course )

student_1 = Student( 'Abdul Jabbar', 21, 45)
student_2 = Student('Maruf Mobin', 22, 96)
student_3 = Student('Munna Mahmud', 22, 72)

teachers = [ teacher_1, teacher_2, teacher_3 ]
courses = [ ds_course, algo_course, py_course ]
students = [student_1, student_2, student_3]

my_school = School(school_name, teachers, courses, students )
my_school.get_students()



    
