
def multiply_numbers(num_1, num_2):
    """
    Multiply two numbers entered by the user and print the product.
    """
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    product = num_1 * num_2

    print(f"Product of {num_1} and {num_2} is {product}")

multiply_numbers()

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


