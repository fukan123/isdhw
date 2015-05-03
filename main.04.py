import math
class Ellipse:
    def Ellipse(self,a,b):
        return(math.pi*a*b)
class Square:
    def Square(self,c):
        return(c*c)
class Rectangle:
    def Rectangle(self,d,e):
        return d*e
class Circle:
    def Circle(self,f):
        return math.pi*f*f
class Myclass(Ellipse,Square,Rectangle,Circle):
    def compute_area(self,shapes):
        for i in range(0,len(shapes)):
            print(shapes[i])
        return(sum(shapes))
q=Myclass()
print("总面积是：",q.compute_area([q.Ellipse(10,20),q.Square(20),q.Rectangle(20,30)，q.Circle(16)]))
