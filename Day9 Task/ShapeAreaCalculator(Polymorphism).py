##6. Shape Area Calculator (Polymorphism) 
##A graphics application needs to calculate the area of different shapes. Create classes 
##Circle, Rectangle, and Triangle, each having an area() method. Demonstrate 
##polymorphism by calling the same method for different objects. 


class Circle:
    def area(self):
        print("Circle Area:", 3.14 * 5 * 5)


class Rectangle:
    def area(self):
        print("Rectangle Area:", 10 * 5)


class Triangle:
    def area(self):
        print("Triangle Area:", 0.5 * 10 * 5)


c = Circle()
r = Rectangle()
t = Triangle()

c.area()
r.area()
t.area()
