import random

def generate_random_number(min_value, max_value):
    """
    Generate a random number within the specified range.

    Parameters:
    min_value (int): The minimum value in the range.
    max_value (int): The maximum value in the range.

    Returns:
    int: A random number within the specified range.
    """
    return random.randint(min_value, max_value)

# Example usage
min_val = 1   # Set the minimum value of the range
max_val = 100000 # Set the maximum value of the range

random_number = generate_random_number(min_val, max_val)
print(f"Random number between {min_val} and {max_val}: {random_number}")
