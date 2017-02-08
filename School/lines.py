class line:
    def __init__(self, x1, y1, x2, y2):
        self.point1 = (x1, y1)
        self.point2 = (x2, y2)

    def __intt__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_length(self):
        return ((self.point2[0]-self.point1[0])**2 + (self.point2[1]-self.point1[1])**2)**0.5

    def get_gradient(self):
        return (self.point2[1]-self.point1[1])/(self.point2[0]-self.point1[0])


a = line(12,351,1,-3)
print(a.get_length())
print(a.get_gradient())