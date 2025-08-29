def validate_numeric_list(data_list):
    """Internal helper to validate input as a non-empty list of numbers."""
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if not data_list:
        raise ValueError("List cannot be empty.")
    for item in data_list:
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements in the list must be numbers. Found non-numeric: {item}")
    return True # Validation passed

def find_max(data_list):
    """
    Finds the maximum value in a list of numbers.
    Raises TypeError if input is not a list or contains non-numeric elements.
    Raises ValueError if the list is empty.
    """
    validate_numeric_list(data_list)
    return max(data_list)

def find_min(data_list):
    """
    Finds the minimum value in a list of numbers.
    Raises TypeError if input is not a list or contains non-numeric elements.
    Raises ValueError if the list is empty.
    """
    validate_numeric_list(data_list)
    return min(data_list)

def calculate_sum(data_list):
    """
    Calculates the sum of numbers in a list.
    Raises TypeError if input is not a list or contains non-numeric elements.
    Raises ValueError if the list is empty.
    """
    validate_numeric_list(data_list)
    return sum(data_list)

def calculate_average(data_list):
    """
    Calculates the average of numbers in a list.
    Raises TypeError if input is not a list or contains non-numeric elements.
    Raises ValueError if the list is empty.
    """
    validate_numeric_list(data_list)
    total_sum = calculate_sum(data_list) # Re-uses sum function, which handles validation
    return total_sum / len(data_list)

if __name__ == "__main__":
    # Example Usage
    my_list = [10, 20, 5, 30, 15]
    print(f"List: {my_list}")
    print(f"Max: {find_max(my_list)}")
    print(f"Min: {find_min(my_list)}")
    print(f"Sum: {calculate_sum(my_list)}")
    print(f"Average: {calculate_average(my_list)}")

    empty_list = []
    try:
        print(f"Max of empty list: {find_max(empty_list)}")
    except (TypeError, ValueError) as e:
        print(f"Error for empty list: {e}")

    non_numeric_list = [1, 2, 'a', 4]
    try:
        print(f"Sum of non-numeric list: {calculate_sum(non_numeric_list)}")
    except (TypeError, ValueError) as e:
        print(f"Error for non-numeric list: {e}")
