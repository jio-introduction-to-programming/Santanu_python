def convert_to_int(x):
    '''
        Task-1 Convert x to int and return the result 
    '''
    result = int(x) # write your code here ! 
    return result 

def find_max_of_numbers(numbers):
    '''
        Task-2 Find and return the maximum number from the list numbers
    '''
    result = max(numbers) # write your code here ! 
    return result 

def get_char_from_num(num):
    '''
        Task-3 Get a character that corresponds to num in Unicode and return the result
    '''
    result = chr(num) # write your code here ! 
    return result 

def get_num_from_char(char):
    '''
        Task-4 Get a number that corresponds to char in Unicode and return the result
    '''
    result = ord(char) # write your code here ! 
    return result 

def calculate_sum_of_numbers(numbers):
    '''
        Task-5 Calculate and return the sum of numbers in the list numbers
    '''
    result = sum(numbers) # write your code here ! 
    return result 

def check_type_of_value(val):
    '''
        Task-6 Check and return the type of val
    '''
    result = type(val) # write your code here ! 
    return result 

def check_any_true_in_list(lst):
    '''
        Task-7 Check if any of the value in the list lst is True
    '''
    result = any(lst) # write your code here ! 
    return result 

def check_all_true_in_list(lst):
    '''
        Task-8 Check if all of the values in the list lst are True
    '''
    result = all(lst) # write your code here ! 
    return result 

def get_current_time():
    '''
        Task-9 Get and return the current time in seconds since the Epoch
    '''
    from datetime import datetime

    current_time = datetime.now().timestamp()

    result = current_time  # write your code here ! 
    return result 
