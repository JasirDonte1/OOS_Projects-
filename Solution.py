# given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# if the number is less than 0, return 1 



def solution(A):
    # write your code in Python 
    compare = 1
    
    A.sort()
    
    if max(A) < 1:
        return 1
    else:   
        for x in A:
            if(x == compare):
                compare += 1
                
        return compare
                
