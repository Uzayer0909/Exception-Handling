try:
    num1,num2 = eval(input("Enter two numbers seperated by comma:"))


    result = num1/num2
    print("Result:",result)


except ZeroDivisionError:
    print("Division by zero is an error")


except SyntaxError:
    print("Comma is missing. So please seperate the numbers using comma.")


finally:
    print("The code will run no matter what ")



