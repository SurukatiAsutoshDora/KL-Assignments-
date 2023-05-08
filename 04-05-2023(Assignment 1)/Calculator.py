#Function for additing  numbers
def Addition(Num_1,Num_2):
    return Num_1+Num_2
#Function for Subtracting numbers
def Subtraction(Num_1,Num_2):
    return Num_1-Num_2
#Function for Multiplying number 
def Multiplication(Num_1,Num_2):
    return Num_1*Num_2
#Function for Dividing numbers
def Divide(Num_1,Num_2):
    return Num_1/Num_2

def take_input():
    Num1=int(input("Please enter the first number:"))
    Num2=int(input("Please enter the second number:"))
    list_of_inputs = [Num1, Num2]
    return list_of_inputs

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
        inputs=take_input()
        print("Num1+Num2 :",Addition(inputs[0], inputs[1]))
        print("\n")
        
    elif User_Input=='-':
        inputs=take_input()
        print("Num1-Num2 :",Subtraction(inputs[0], inputs[1]))
        print("\n")
        
    elif User_Input=='*':
        inputs=take_input()
        print("Num1*Num2 :",Multiplication(inputs[0], inputs[1]))
        print("\n")
        
    elif User_Input=='/':
        inputs=take_input()
        print("Num1/Num2 :",Divide(inputs[0], inputs[1]))
        print("\n")  
        
    elif User_Input== "0":
        exit(0)
    
    else:
        print("invalid choice")    
       





    