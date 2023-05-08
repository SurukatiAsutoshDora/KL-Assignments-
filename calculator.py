"""
This is calculator program written in python using the class and objects.
"""
# declaring a Class


class Clc():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
# Function for additing  numbers

    def addition(self):
        """ 
          Function for Adding numbers 
        """
        return self.num_1+self.num_2
# Function for Subtracting numbers

    def subtraction(self):
        """ 
          Function for Subtraction numbers 
        """
        return self.num_1-self.num_2
# Function for Multiplying numbers

    def multiplication(self):
        """ 
          Function for multiplying numbers 
        """
        return self.num_1*self.num_2

    def divide(self):
        """ 
          Function for Dividing numbers 
        """

        return self.num_1/self.num_2


def take_input():
    num1 = int(input("Please enter the first number:"))
    num2 = int(input("Please enter the second number:"))
    list_of_inputs = [num1, num2]
    return list_of_inputs


# choices for user
while True:
    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Enter your Requirement\n")
    print("+ for Addition of two number")
    print("- for Subtraction of two number")
    print("* for Multiplication of two number")
    print("/ for Divide of two number")
    print("0 to Exit\n")

    # User_Input is taken
    user_Input = input("Please enter your choice from + - * / 0 \n")
    # Operation takes place according to the user choice
    if user_Input == '+':
        inputs = take_input()
        obj = Clc(inputs[0], inputs[1])
        print("Num1+Num2 :", obj.addition())
        print("\n")

    elif user_Input == '-':
        inputs = take_input()
        obj = Clc(inputs[0], inputs[1])
        print("Num1-Num2 :", obj.subtraction())
        print("\n")

    elif user_Input == '*':
        inputs = take_input()
        obj = Clc(inputs[0], inputs[1])
        print("Num1*Num2 :", obj.multiplication())
        print("\n")

    elif user_Input == '/':
        inputs = take_input()
        obj = Clc(inputs[0], inputs[1])
        print("Num1/Num2 :", obj.divide())
        print("\n")

    elif user_Input == "0":
        break

    else:
        print("invalid choice")
