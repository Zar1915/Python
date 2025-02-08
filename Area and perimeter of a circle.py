class circle():
    def __init__(self, r, pi):
        self.radius = r
        self.pi = pi
    def Circlearea(self):
        return self.pi * self.radius *self.radius
NewCircle = circle(12, 3.14) 
print("Dimension of circle pi:%d radius:%d"%(NewCircle.radius, NewCircle.pi))
print("Area of circle", NewCircle.Circlearea())
 
def calculate_perimeter(self):
    return 2 * NewCircle.pi * NewCircle.radius
NewCircle = circle(12, 3.14)
print("Dimension of circle pi:%d radius:%d"%(NewCircle.radius, NewCircle.pi))
radius = 12
perimeter = calculate_perimeter(radius)
print(f"The perimeter (circumference) of the circle is: {perimeter}")

