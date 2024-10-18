class Circle:
    def __init__(self,radius,pai):
        self.radius=radius
        self.pai=pai

    def circle_circumference(self):
        value_of__circumference=2 * self.pai * self.radius
        return value_of__circumference

    def circle_area(self):
        area=self.pai * self.radius**2
        return area
           

