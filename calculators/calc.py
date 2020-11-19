#!/usr/bin/python3
import sys
"""
Basic Calculation Using Python 3, 
"""
# reject if this file called as module
if __name__ != "__main__":
    print("you must execute this directly")
    sys.exit()


print("""
Available Operators:
    (+) : Addition
    (-) : Substraction
    (*) : Multiplication
    (/) : Division

(i) : for decimal value use dot(.) instead of comma ex: 2.4
(i) : you also can do this : (2+2)*2 -> 8
    """)

# Adding our operator inside of list
operators = ["+","-","/","*"]

# let create input event
calculate = input("calculate> ")


"""
WARNING : 
Since I use eval() to calculating user input
i will take care of this app security
"""

# we will add a scene if the user not adding any operators then
# we will run the Interactive Schema
def isSafe(string):
    # there will be other way to do it, but i will use this:
    global operators
    # Extract operator from our input
    for x in operators:

        string = string.replace(x,"")
        # if input like this : 2+2 . that will be 22

    # we can check if the input is safe before we call eval()

    """
    Let's create a simulation:

        >>> calculate = input("Calculate :")
            "2+2"
        >>> string = calculate
        >>> for x in operator:
        ...     string.replace(x,"")
        >>> print(string)
            "22"
        >>> string.isnumeric()
            True

        Cool. that input is safe,
        but if we enters a floated number (decimal) it will return False

        >>> string = "4.2"
        >>> string.isnumeric()
            False
    """

    # Extract "." in our input too
    string = string.replace(".","")
    
    string = string.replace("(","")
    string = string.replace(")","")
    # if input has pass the test, return True, False otherwise
    if string.isnumeric():
        return True
    else:
        print("you only can pass numbers and operators only!")
        return False

def Interactive_mode(string):
    if isSafe(string):
        print("No Operators detected, running on interactive mode")
        operations = string
        operator = input("operator> ")
        if operator in operators:
            operations += operator
            print("operations> " + str(operations))
            number = input("number> ")
            if isSafe(operations+number):
                operations += number
                print("operations> " + str(operations))
                print("result> "+ str(eval(operations)))
        else:
            print(f"{operator} not available in our operators")

# check the input 
interactive = True
for x in operators :
    if x in calculate:
        interactive = False
        break


if len(calculate) > 0 and not calculate.isspace():
    if interactive:
        Interactive_mode(calculate)
    else:
        if isSafe(calculate):
            try:
                result = eval(calculate)
                print(result)
            except (SyntaxError):
                print(f"Cannot Calculate this operations : {calculate}")
        else:
            print(f"Cannot Calculate this operations : {calculate}")
elif calculate.isspace():
    print("Whitespace are not allowed")
elif len(calculate) == 0:
    print("Must Enter a number")
