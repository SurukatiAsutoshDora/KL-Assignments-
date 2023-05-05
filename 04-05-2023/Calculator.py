#Function for additing  numbers
def Addition(Num_1,Num_2):
    return Num_1+Num_2

#Function for Subtracting numbers
def Subtraction(Num_1,Num_2):
    return Num_1-Num_2

#Function for Multiplying numbers   
def Multiplication(Num_1,Num_2):
    return Num_1*Num_2

#Function for Dividing numbers
def Divide(Num_1,Num_2):
    return Num_1/Num_2

#choices for user
while(True):
    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Enter your Requirement\n")
    print("+ for Addition of two number")
    print("- for Subtraction of two number")
    print("* for Multiplication of two number")
    print("/ for Divide of two number")
    print("0 to Exit\n")


    #User_Input is taken
    User_Input=input("Please enter your choice from + - * / 0 \n")

    #Operation takes place according to the user choice
    if User_Input=='+':
        Num1=int(input("Please enter the first number:"))
        Num2=int(input("Please enter the second number:"))
        print("Num1+Num2 :",Addition(Num1,Num2))
        print("\n")
        
    elif User_Input=='-':
        Num1=int(input("Please enter the first number:"))
        Num2=int(input("Please enter the second number:"))
        print("Num1-Num2 :",Subtraction(Num1,Num2))
        print("\n")
        
    elif User_Input=='*':
        Num1=int(input("Please enter the first number:"))
        Num2=int(input("Please enter the second number:"))
        print("Num1*Num2 :",Multiplication(Num1,Num2))
        print("\n")
        
    elif User_Input=='/':
        Num1=int(input("Please enter the first number:"))
        Num2=int(input("Please enter the second number:"))
        print("Num1/Num2 :",Divide(Num1,Num2))  
        print("\n")  
        
    elif User_Input== "0":
        break
    
    else:
        print("invalid choice")    
       





    