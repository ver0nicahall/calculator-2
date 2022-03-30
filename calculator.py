"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
calculator_on = True
print("The calculator has turned on.")

#read input 
while True:
    user_input = input('What would you like to perform? ')
    tokens = user_input.split(' ')
    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) > 2:
        num2 = tokens[2]

    if operator == 'q':
        break
        #if the first token is q
            #quit

    #add
    if operator == '+':
        result = add(float(num1), float(num2))

    #subtract
    if operator == '-':
        result = subtract(float(num1), float(num2))
    
    # #multiply
    if operator == '*':
        result = multiply(float(num1), float(num2))

    #divide
    if operator == '/':
        result = divide(float(num1), float(num2))
    
    #square
    if operator == 'square':
        result = square(float(num1))

    #cube
    if operator == 'cube':
        result = cube(float(num1))

    #power
    #mod

    #print result to screen
    print('Result: ' + str(result))