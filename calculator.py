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
    num2 = tokens[2]


    print('User input: ' + str(user_input))
    print('Tokens: ' + str(tokens))
    print('operator: ' + str(operator))
    print('num1: ' + str(num1))
    print('num2: ' + str(num2))

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
    
    #print result to screen
    print('Result: ' + str(result))