class Employee:
    def __init__( self, name, id , salary, position, exprience ):
        self.name = name
        self.id = id
        self.salary = salary
        self.position = position    
        self.exprience = exprience


class Developer( Employee ):
    def __init__( self, name, id , salary, position, tech, focus, exprience ):
        self.tech = tech
        self.area_of_work = focus
        super().__init__( name, id , salary, position, exprience )

    
class Testing( Employee ):
    pass

class Sales( Employee ):
    pass

class TechLead( Employee ):
    def __init__( self, name, id , salary, position, team ):
        self.team = team
        super().__init__( name, id , salary, position )