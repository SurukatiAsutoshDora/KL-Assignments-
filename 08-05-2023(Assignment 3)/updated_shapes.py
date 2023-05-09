import math
class Rectangle:
    """
    this class is used to take the parameters of a rectangle and print its area and perimeter
    """

    def __init__(self, rectangle_length, rectangle_breadth):
        self.length = rectangle_length
        self.breadth = rectangle_breadth

    def calculate_area(self):
        """
         this function  which is used to calculate the area of a rectangle
        """
        area = self.length * self.breadth
        print("the area of a rectangle is", area)

    def calculate_perimeter(self):
        """
         this function  which is used to calculate the area of a circle
        """
        perimeter = 2*(self.length + self.breadth)
        print("the perimeter of a rectangle is", perimeter)


class Circle:
    """
    this class is used to take the radius of a circle and print its area and perimeter
    """

    def __init__(self, circle_radius):
        self.radius = circle_radius

    def calculate_area(self):
        """
         this function  which is used to  calculate the area of a circle
        """
        area = math.pi * self.radius ** 2
        print("the area of a circle is", area)

    def calculate_perimeter(self):
        """
         this function  which is used to calculate the area of a circle
        """
        perimeter =2 * math.pi * self.radius
        print("the perimeter of a circle is", perimeter)


class Triangle:
    """
    this class is used to take all the parameters of a triangle and print its area and perimeter
    """

    def __init__(self, triangle_side_1, triangle_side_2, triangle_side_3):
        self.side1 = triangle_side_1
        self.side2 = triangle_side_2
        self.side3 = triangle_side_3

    def calculate_area(self):
        """
         this function  which is used to calculate the area of a triangle
        """
        semi = (self.side1 + self.side2 + self.side3)/2
        area = (semi * (semi - self.side1) *
                (semi - self.side2)*(semi - self.side3))**0.5
        print("the area of a triangle is", area)

    def calculate_perimeter(self):
        """
         this function which is used to calculate the area of a triangle
        """
        perimeter = self.side1+self.side2+self.side3
        print("the perimeter of a triangle is", perimeter)


class Square:
    """
    this class is used to take side of a square and print its area and perimeter
    """

    def __init__(self, square_side):
        self.side = square_side

    def calculate_area(self):
        """
         this function  which is used calculate the area of a square
        """
        area = self.side*self.side
        print("the area of a square is", area)

    def calculate_perimeter(self):
        """
         this function  which is used to take the calculate the area of a square
        """
        perimeter = 4*self.side
        print("the perimeter of a square is", perimeter)


while True:
    print("Please enter in lowercase")
    print("Enter rect for finding area and perimeter of a rectangle")
    print("Enter cir for finding area and perimeter of a circle")
    print("Enter tri for finding area and perimeter of a triangle")
    print("Enter squ for finding area and perimeter of a square")
    print("0 to exit")

    user_Input = input("Please enter your choice \n")

    if user_Input == "rect":
     try:
         length = int(input("Enter the Length : "))
         breadth = int(input("Enter the Breadth : "))
         if length < 0 or breadth < 0:
             raise ValueError("Length and Breadth Must be positive values")
     except ValueError as error:
         print("::Invalid input::", str(error))
         continue
     obj_rectangle = Rectangle(length, breadth)
     obj_rectangle.calculate_area()
     obj_rectangle.calculate_perimeter()

    elif user_Input == "cir":
        try:
         side = int(input("Enter the radius : "))
         if side<0:
              raise ValueError("Radius must be positive")
        except ValueError as error:
            print("::Enter a valid input::", str(error))
            continue
        obj_circle = Circle(side)
        obj_circle.calculate_area()
        obj_circle.calculate_perimeter()

    elif user_Input == "tri":
        print("Enter first side, second side, third side ")
        try:
         side1 = int(input("Enter the first side : "))
         side2 = int(input("Enter the second side : "))
         side3 = int(input("Enter the third side : "))
         if side1<0 or side2<0 or side3<0:
             raise ValueError("length of the side should always be positive")
        except ValueError as error:
            print("::Enter a valid input::",str(error))
            continue
        obj_triangle = Triangle(side1, side2, side3)
        obj_triangle.calculate_area()
        obj_triangle.calculate_perimeter()

    elif user_Input == "squ":
        try:
         side = int(input("enter the length of a side : "))
         if side<0:
           raise ValueError("Length of the side must be positive")
        except ValueError as error:
            print("::Enter a valid input::", str(error))
            continue
        obj_square = Square(side)
        obj_square.calculate_area()
        obj_square.calculate_perimeter()

    elif user_Input == "0":
        break

    else:
        print("Please enter the correct choice or use lowercase")