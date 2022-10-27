class School:
    # Constractor
    def __init__( self, name, address, principal = ' '):
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade( self, name, teacher ):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)

    def remove_grade( self, name ):
        idx = 0
        for i , grade in enumerate( self.grades ):
            if grade.name == name:
                idx = i
        del self.grades[idx]

class Grade:
    # Constractor
    def __init__( self, name, teacher ):
        self.students = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'Class of {self.name} with Teacher {self.teacher}'

    def __del__(self):
        print(f'Deleting {self.name} class with teacher {self.teacher}')

oxford = School('Oxford kid Academy', 'Mirpur', 'Obayed Alam')
oxford.add_grade('class 3', 'Osman Gani')
oxford.add_grade('class 5', 'Neha mam')  
oxford.add_grade('class 8', 'Rajib Sir')  


print(oxford.grades)
oxford.remove_grade('calss 5')
print(oxford.grades)
