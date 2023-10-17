def divide(dividend, divisor):
    """
    Divides the dividend by the divisor and returns the result.

    Args:
        dividend (float or int): The number to be divided.
        divisor (float or int): The number to divide by.

    Returns:
        float or int: The quotient of the division.

    Raises:
        ZeroDivisionError: If the divisor is zero.

    """
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")
    
    quotient = dividend / divisor
    print(f"the result of dividing {dividend} by {divisor} is{quotient}")

divide (10, 6)

import math 

def calc_log(number):
    """
    Calculates the natural logarithm of a given number and displays the result.

    Args:
        number (float or int): The number for which to calculate the logarithm.

    Returns:
        None

    """
    log = math.log(number)
    print(f"The logarithm of {number} is: {log}")

calc_log(10)  

    