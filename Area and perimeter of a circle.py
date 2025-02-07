class circle():
    def __init__(self, r, pi):
        self.radius = r
        self.pi = pi
    def Circlearea(self):
        return self.radius
NewCircle = circle(12, 10) 
print("Dimension of circle pi:%d radius:%d"%(NewCircle.radius, NewCircle.pi))
print("Area of circle", NewCircle.Circlearea())
        
