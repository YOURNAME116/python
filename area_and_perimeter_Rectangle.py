class rectangle:
    def __init__(self,length,width) :
        self.length= length
        self.width=width
    def area(self):
        area = self.length*self.width
        return area
    def parameter(self):
        perimeter = 2*(self.length + self.width)
        return perimeter

if __name__ == '__main__':
    rectangle1=rectangle(4,9)   
    print(rectangle1.area())
