"""
This program takes shape as a user input and then gives the area and perimeter respectively.
It has a pylint score of 9.74
"""
# declaring a class called shape


class Rectangle:
    """
    this class is used to take the length and breadth of a rectangle and print its area and perimeter
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
        area = self.radius * self.radius
        print("the area of a circle is", area)

    def calculate_perimeter(self):
        """
         this function  which is used to calculate the area of a circle
        """
        perimeter = 2 * 3.14*self.radius
        print("the perimeter of a circle is", perimeter)


class Triangle:
    """
    this class is used to take all the parameters of a triangle and print its area and perimeter
    """

    def __init__(self, tri_base, tri_height, tri_side_1, tri_side_2, tri_side_3):
        self.base = tri_base
        self.height = tri_height
        self.side1 = tri_side_1
        self.side2 = tri_side_2
        self.side3 = tri_side_3

    def calculate_area(self):
        """
         this function  which is used to calculate the area of a triangle
        """
        area = 0.5 * self.base * self.height
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
         this function  whihch is used to take the calculate the area of a square
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
        length = int(input("Enter the Length"))
        breadth = int(input("Enter the Breadth"))
        obj_rectangle = Rectangle(length, breadth)
        obj_rectangle.calculate_area()
        obj_rectangle.calculate_perimeter()

    elif user_Input == "cir":
        side = int(input("Enter the radius"))
        obj_square = Circle(side)
        obj_square.calculate_area()
        obj_square.calculate_perimeter()

    elif user_Input == "tri":
        print("Enter first side, second side, third side, base and height ")
        side1 = int(input("Enter the first side"))
        side2 = int(input("Enter the second side"))
        side3 = int(input("Enter the third side"))
        base = int(input("Enter the base"))
        height = int(input("Enter the height"))
        obj_triangle = Triangle(base, height, side1, side2, side3)
        obj_triangle.calculate_area()
        obj_triangle.calculate_perimeter()

    elif user_Input == "squ":
        side = int(input("enter the length of a side"))
        obj_triangle = Square(side)
        obj_triangle.calculate_area()
        obj_triangle.calculate_perimeter()

    elif user_Input == "0":
        break

    else:
        print("Please enter the correct choice or use lowercase")
