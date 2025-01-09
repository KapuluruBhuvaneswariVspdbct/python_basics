print("EXCEPTION HANDLING\n")
def exception_handling():
    try:
        num1 = int(input("enter the numerator"))
        num2 = int(input("enter the denominator"))
        divide = num1 / num2
        return divide
    except ValueError:
       return "values is not correct"
    except ZeroDivisionError :
        return "num cant divide by zero"
    finally:
       print("Division operation uses the 2 operands")
    #finally is the main code that is to be worked even if the code has no errors or the code has errors
exception_call = exception_handling()
print(exception_call)


number = int(input("enter a number greater than 10 to check the raise exception"))
if number > 10 :
    raise ValueError("The entered valueis invalid ")