
def add_one_to_number(x):
    '''
        Task-1 Write the code below to add 1 to a number 
        and remove the pass statement 
    '''
    result = x + 1  # write your code here and replace None with the actual value 
    return result 

def add_two_numbers(x, y):
    '''
        Task-2 remove the pass statement and return the sum of 
        2 numbers  
    ''' 
    result = x + y # write your code here ! 
    return result 

def subtract(x, y):
    '''
        Task-3 subtract y from x and return the result 
    '''
    result = x - y # write your code here ! 
    return result 


def sum_first_n_natural_numbers(n):
    '''
        Natural numbers are 1 -> infinity 
    '''
    if n < 1:
        return None 
    result = n*(n+1)/2 # write your code here 
    return result 

def divide_x_by_y_float(x, y):
    '''
        Division by zero is not defined 
        Return the result of x divided by y as a float 
    '''
    if y == 0:
        return None 
    result = float(x/y) # replace None with your code 
    return result 

def divide_x_by_y_numeric(x, y):
    '''
        Return the result of x divided by y as a numeric without decimals 
    '''
    if y == 0:
        return None 
    result = x//y # replace None with your code 
    return result 

def remainder_x_by_y(x, y):
    '''
        Remainder when x is divided by y 
    ''' 
    result = x%y # replace None with your code 
    return result 
