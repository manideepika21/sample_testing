def factorial(n):
    """Calculate the factorial of a number recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}")
