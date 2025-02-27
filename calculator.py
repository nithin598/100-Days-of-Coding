def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dict = {"+":add,"-":subtract,"*":multiply,"/":divide,}



result_ = 0
continue_with_result = 'yes'
f_number = float(input("Enter first number:"))

while continue_with_result == 'yes':

    operation_ = input("Enter the Operation to Perform:\n"
                  "+ for Addition\n"
                  "- for Subtraction\n"
                  "* for Multiplication\n"
                  "/ for Division\n")
    s_number = float(input("Enter second number:"))

    print(calculator_dict[operation_](f_number,s_number))
    f_number = calculator_dict[operation_](f_number,s_number)
    continue_with_result = input("You want to continue with previous result?\n"
                                 "yes  --> to continue\n"
                                 "no   --> to restart\n")
    if continue_with_result == "no":
        print("\n"*100)
        continue_with_result = "yes"
        f_number = float(input("Enter first number:"))

