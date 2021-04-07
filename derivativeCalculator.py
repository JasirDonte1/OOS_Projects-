'''
I created a bug/situation where negative exponents are not being evaluated properly because of re.split() in enqueue() line examine 92

add/work on brackets logic [ ] ( ) explore using bracket logic to solve negative exponent issue.

add more comments to code 


program semi-functional. still can't properly evaluate negative exponents in terms or evaluate division/multiplication 


today worked on driver, multiple executions, findDerivative()

fixed issued to properly evaluete constants as 0.

fixed the issue revolving arround queing up terms with negative coefficients - enqueue()

'''


import re


#derivative calculator   d/dx

operations_array = ['+','-','/','*']
term_queue = []
operations_queue = []

#evaluate if the term is a valid mathnatical term

#break up raw number in to individual terms
#keep terms in a queue and operation symbols in a queue

#create a function that returns the derivative of a single term.
#append returned values to the derivative queue

#while a term exists in the derivative queue, pop and stringTo an operation to converted number

#METHOD: ISVALIDTERM()
def isValidTerm(raw_num): #returns true if the passed string is a valid trig term

    if(raw_num[0] in operations_queue):term=term[1:]

    check_one = False

    #if there is no (+,-,/,*) symbol in the string return False
    for operation in operations_array:
        if operation in raw_num:
            check_one = True    #terms exist

            
    #if back to back symbols are found return False
    if check_one == True:
        previous_term = ''
        #returns false if there are back to back characters that are operations
        for char in raw_num:
            if char in operations_array:
                if previous_term in operations_array:
                    return False
            previous_term = char

    else:
        #terms does not exist
        #if there exists a valid single term
        #for each character in the term
        #if the char is a letter in alphabet a number or '^' ... continue
        #else return false

        for char in raw_num:
            if char.isalpha():
                pass
            elif char.isnumeric():
                pass
            elif char == '^':
                pass
            else:    #if there is any character that is not a letter or number or ^, like $,false is returned 
                return False
            
    return True


#METHOD: ENQUEUE  
def enqueue(raw_num):
    print('raw_num', raw_num)
    op_sub_array =[]
    
    for x in raw_num: 
        if x in operations_array: 
            op_sub_array.append(x)
            
    q = re.split(r"\+|\-|\*|\\", raw_num)

    if q[0] == '':
        q = q[1:]
        q[0] = '-'+q[0]
        
        op_sub_array = op_sub_array[1:]

    count = 1

    for x in op_sub_array:
        q[count] = op_sub_array[count-1]+q[count]
        count += 1
    print('queue', q)
    return q



#METHOD: DERIVATIVE_OF
def derivativeOf(term):   #function returns the derivative of a single term as a string
    derivative = 0
    coefficient = 0
    power = 0

    if(term[0] == '+'):
        term = term[1:]
        
    if '^' in term: #if there is an exponent involved
        
        if(term[0] == 'x'):
            expression = term.split('^')
            derivative = expression[1] + 'x'
        
        elif(term[0].isnumeric()):
            expression = term.split('^')
            
            x_split = expression[0].split('x')
            power = int(expression[1])
            coefficient = int(x_split[0])
            coefficient = coefficient*power
            
            power = power - 1 

            if(power > 1):
                derivative = str(coefficient) + 'x^' + str(power)
            elif(power == 1):
                derivative = str(coefficient) + 'x'
            elif(power == 0):
                derivative = str(coefficient)
            elif power < 0:
                derivative = str(coefficient) + 'x^' + str(power)
            
        elif(term[0] == '-'):

            exp = ['-']
            term = term[1:]  #x^7

            print('term: ', term)

            expression = term.split('^')  #[x,7]
            print('split', expression)
            print('exp: ', expression)
            power = int(expression[1])

          

            if (expression[0] == 'x'):  #-x

                if power > 1:
                    coefficient = power*-1
                    power = power-1
                    derivative = str(coefficient) + 'x^'+ str(power)
                elif power == 1:
                    derivative = '-x'
                elif power == 0:
                    derivative = '-1'
                elif power < 0:
                    coefficient = -1*power
                    power = power - 1
                    print(power)
                    derivative = str(coefficient) + 'x^' + str(power)
                

            else:
                x_split = expression[0].split('x')

                coefficient = int(x_split[0])
                coefficient = coefficient*power
                
                if(power > 1):
                    power = power-1
                    derivative = '-' + str(coefficient) + 'x^' + str(power)
                elif(power == 1):
                    derivative = '-' + str(coefficient) + 'x'
                elif(power == 0):
                    derivative = '-' + str(coefficient)
                elif power < 0:
                    power = power -1 
                    derivative = str(coefficient) + 'x^' + str(power)
                    derivative = derivative[1:]
                    
        
    else:    #if not exponent is involved
        print('ddd',term)
            
        
        if(term == 'x'):
            derivative = '1'
        elif(term == '-x'):
            derivative = '-1'
        elif 'x' not in term:
            derivative = '0'
        else:
            expression = term.split('x')
            derivative = expression[0]


        print('end of if statement')
        
    return derivative

def findDerivative(inp):
    
    if(isValidTerm(inp)):     #if the entry/input is valid
        term_queue = enqueue(inp)

        for m in term_queue:
            print(type(m))
        #TAKE THE DERIVATIVE OF EACH TERM#
        expression = []
        for t in term_queue:
            u = derivativeOf(t)
            print(u)
            if u == '0':
                pass
            else:
                expression.append(u)
        print('expression: ',expression)
        #CODE TO STRING TOGETHER EXPRESSION[]#
        to_string = ''
        for r in expression:
            to_string += r
        print(to_string)
            
    else:
        #raw number is not a valid number
        print('Enter a valid Number')



###### FUNCTIONS DEFINED ABOVE ########


##### DRIVER #####
end = False

while end == False:
    i = input('d/dx Calculator \nEnter an expression (or type "end" to end program): ')
    if i == 'end':
        end = True
    else:
        findDerivative(i)
            
    



