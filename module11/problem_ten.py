import math
class Distance:
    def __init__(self, x1,y1,x2,y2):
        self.result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    def output(self):
        return self.result
 
result = Distance(2,2,1,1)
print(result.output())