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



    