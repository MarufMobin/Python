numbers= [10,20,10,40,50,60,70]
target = 130

class Sum_pair:
    def __init__(self, numbers , target ):
        for i, num in enumerate(numbers):
            if numbers[i] + numbers[i+1] == target:
                print(i+1, " ", i+2)
                return

my_sum = Sum_pair( numbers, target )


numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
class Result:
    def __init__(self, target, lst):
        self.target = target
        self.lst = lst
 
    def find_target(self):
        res = []
        for i, val in enumerate(self.lst):
            for j in self.lst[i+1:]:
                if val + j == target:
                    res = [i+1, i+2]
        return res
 
r = Result(target,numbers)
print(r.find_target())