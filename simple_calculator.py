

'''
accept string of a simple arithmatic statement between two values.

Skills desplayed:
use of objects/class
use of member functions
remove whitespaces from a string
if/else statement
string concatention 
type converstion 


'''
class Calculator:

#arithmatic functions add, subtract, divide, multiply
    
    def findSum (self, v1, v2):   #v1 = value_one, v2 = value_two 
        v3 = v1 + v2
        return v3
    def findDifference(self, v1, v2):
        v3 = v1 - v2
        return v3
    def findQuotient (self, v1, v2):
        v3 = v1 / v2
        return v3
    def findProduct (self, v1, v2):
        v3 = v1 * v2
        return v3

# main/driver
user_input = input('Enter an arithmatic statement ')
user_input = ''.join(user_input.split())  #remove whitespaces

operations = ["+","-","/","*"]  #operations array
counter = 0 #iterator to track the proper operation performed.


x = user_input.split(operations[counter])  #primes loop to find correct operation to be performed. Split will occur when operation symbol from user input matches symbol in operations array
while (len(x) < 2):       #will iterate throught operations until correct operation is found
    counter = counter + 1  #tracks which operation was performed 
    x = user_input.split(operations[counter])     #split creates an array holding value 1 and value 2 in slots 0 and 1 in the array 


calculator_1 = Calculator()     #instantiate new Calculator object 

'''
If else statement determines which operation should be performed based on the value of the counter
variable. Counter value corresponds to the operations place in the "operations" array.

y = the calcualted answer to the arithmatic problem
'''

if(counter == 0):  
    y = calculator_1.findSum(float(x[0]), float(x[1])) #wraps string values to be conveted to floats 
elif(counter == 1):
    y = calculator_1.findDifference(float(x[0]), float(x[1]))
elif(counter == 2):
    y = calculator_1.findQuotient(float(x[0]), float(x[1]))
elif(counter == 3):
    y = calculator_1.findProduct(float(x[0]), float(x[1]))
   

#print statement prints orginal arithmetic statement and calculated value from class method    

print(user_input + " = " + str(y)) # str() converts string back in to float 
    

