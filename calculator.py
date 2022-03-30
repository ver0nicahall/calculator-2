"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
calculator_on = True
print("The calculator has turned on.")

while calculator_on == True:
    #ask for numbers
    user_input = input("What input would you like to perform? Please enter (operator) (number) (number)")
    #split input into tokens 
    tokens = user_input.split(' ')

    operator = user_input[0]
    num1 = user_input[1]
    num2 = user_input[2]

    #perform operation
    #add
    if operator == '+':
        result = add(float(num1), float(num2))

    #print result


    #if the user decides to quit
    if input == 'q':
        #turn calculator off 
        print("The calculator is turning off. Goodbye!")
        calculator_on = False
        break
 print('Your result is ' + str(result))