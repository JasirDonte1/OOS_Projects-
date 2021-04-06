'''

today I started designing the skeleton and logic of how the program will work.

next I need to start programming that logic 

'''



#derivative calculator
raw_number =  "2x^2+3x-4"
operations_array = ['+','-','/','*','^']

term_queue = []
operations_queue = []
derivative_queue = []

#actual derivative = 4x+4 = (4x+3+1)

#evaluate if the term is a valid mathnatical term

#break up raw number in to individual terms
#keep terms in a queue and operation symbols in a queue

#create a function that returns the derivative of a single term.
#append returned values to the derivative queue

#while a term exists in the derivative queue, pop and stringTo an operation to converted number


def isValidTerm(raw_num): #returns true if the passed string is a valid trig term
    is_valid = True
    #not_valid = ['++','--','//','**','^^', '+-', '-+', '+/', '/+','-/','/-','+*', '*+','+^','^+','']
    check_one = False

    #if there is no (+,-,/,*,^) symbol return False

    for operation in operation_array:
        if operation in raw_number:
            check_one = True 
    
    #if back to back symbols are found return False
    

    for char in raw_num:
        print(char+1)
        


    return is_valid
    
    
def enqueue (raw_num):    #raw num passes the string of user input 


    return 0

def derivativeOf(term):   #function returns the derivative of a single term as a string
    derivative = 0

    return derivative


###### FUNCTIONS DEFINED ABOVE ########

try:
    




    


   

    
except:
    print('something went wrong')
