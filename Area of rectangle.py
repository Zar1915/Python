class rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def Rectanglearea(self):
        return self.length*self.width
NewRectangle = rectangle(12, 10) 
print("Dimension of rectangle length:%dwidth%d"%(NewRectangle.length, NewRectangle.width))
print("Area of rectangle", NewRectangle.Rectanglearea())