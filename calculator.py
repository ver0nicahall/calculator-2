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

    #if anything is a q = quit
    if 'q' in tokens:
        print('You have turned the power off. Shutting down.')
        break 

    #set operator and numbers
    operator = tokens[0]
    num1 = tokens[1]

    #optional third number
    if len(tokens) > 2:
        num2 = tokens[2]
    
    #if they enter not a number 
    if (tokens[1].isdigit() == False) or (tokens[2].isdigit() == False): 
        print("You have entered an invalid number. Please try again.")
        continue

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
    if operator == '**':
        result = power(float(num1), float(num2))

    #mod
    if operator == '%':
        result = mod(float(num1), float(num2))
    #print result to screen
    print('Result: ' + str(result))