


def check_even_odd(number):
    """Determine if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

# Get user input
try:
    num = int(input("Enter an integer: "))
    print(check_even_odd(num))
except ValueError:
    print("Please enter a valid integer!")