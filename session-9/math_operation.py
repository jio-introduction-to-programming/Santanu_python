def add(a,b):
    """
    Function to add two numbers and return the results.\n
    Args:
        a = Input number one.\n
        b = Input number two.\n
    Returns:
        return result
    """

    return a+b

def sub(a,b):
    """
    Function to add two numbers and return the result.\n
    Args:
        a = Input number one.\n
        b = Input number two.\n
    Returns:
        return result
    """
    return a-b

def mul(a,b):
    """
    Function to multiply two numbers and return the result.\n
    Args:
        a = Input number one.\n
        b = Input number two.\n
    Returns:
        return result
    """

    return a*b

def div(a,b):
    """
    Function to divide two numbers and return the result.\n
    Args:
        a = Input number one.\n
        b = Input number two.\n
    Returns:
        return result
    """

    try:
        result = a/b
    except ZeroDivisionError:
        print("It is not possible to divide by the zero")

    return result