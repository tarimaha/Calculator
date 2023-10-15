def multiply_numbers(num_1, num_2):
    """
    Multiply two numbers entered by the user and print the product.
    """
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))

    product = num_1 * num_2

    print(f"Product of {num_1} and {num_2} is {product}")

multiply_numbers()