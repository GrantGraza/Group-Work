# calculator.py
# Grant Graza, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#

first_value = int(input('Enter your first value:'))                 # First 5 lines of code lets user input 3 integer values and 2 operators between the values
first_operator = input('Enter your first operator:')
second_value = int(input('Enter your second value:'))
second_operator = input('Enter your second operator:')
third_value = int(input('Enter your third value:'))

if first_operator == '/' :                                          #Activates when the first operator is division
    new_value = first_value / second_value                          #Divides the first integer input to the second integer input creating a new value
    if second_operator == '/':                                      #New value is divided to third value
       answer = new_value / third_value
    elif second_operator == '*':                                    #New value is multiplied to third value
        answer = new_value * third_value
    elif second_operator == '+':
        answer = new_value + third_value                            #New value is added to third value
    elif second_operator == '-':
        answer = new_value - third_value                            #Third value is subtracted from new value

elif first_operator == '*' :                                        #Activates when the first operator is multiplication
    new_value = first_value * second_value                          #Multiplies the first integer input to the second integer input creating a new value
    if second_operator == '/':
       answer = new_value / third_value                             #New value is divided by third value
    elif second_operator == '*':
        answer = new_value * third_value                            #New value is multiplied to third value
    elif second_operator == '+':
        answer = new_value + third_value                            #New value is added to third value
    elif second_operator == '-':
        answer = new_value - third_value                            #Third value is subtracted from new value

elif first_operator == '+' :                                        #Activates when the first operator is addition
    if second_operator == '/':                                      #Second value is divided by third value, first value is added after
       answer = second_value / third_value + first_value
    elif second_operator == '*':
        answer = second_value * third_value + first_value           #Second value is multiplied by third value, first value is added after
    elif second_operator == '+':
        answer = second_value + third_value + first_value           #First value is added to second value, third value is added after
    elif second_operator == '-':
        answer = first_value + second_value - third_value           #First value is added to second value, the sum is subtracted by the third value

elif first_operator == '-' :                                        #Activates when the first operator is subtraction
    if second_operator == '/':                                      #Second value is divided by third value, the first value is subtracted by the quotient
       answer = first_value - (second_value / third_value) 
    elif second_operator == '*':                                    #Second value is multiplied by the third value, the first value is subtracted by the product
        answer = first_value - (second_value * third_value) 
    elif second_operator == '+':                                    #First value is subtracted by the second value and third value is added after
        answer = first_value - second_value + third_value
    elif second_operator == '-':                                    #First value is subtracted by the second value and the third value
        answer = first_value - second_value - third_value


print ('\nEntered expressions is:', first_value, first_operator, second_value, second_operator, third_value) #Displays the equation from the input values and operators
print ('Your final answer is:', int(answer))                        #Displays the final answer

print("Hi!!!!!!!!!")