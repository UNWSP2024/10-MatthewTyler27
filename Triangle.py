#Matthew Tyler
#11/7/25
#Triangle

class Triangle():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
         

T1 = Triangle(3,4,5)
calculate = T1.perimeter()
print(calculate)
