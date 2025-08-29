# NumberFileProcessor.py

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip()]
            return numbers
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []
    except ValueError:
        print("File contains non-numeric data.")
        return []

def calculate_sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return total, average

if __name__ == "__main__":
    file_name = "numbers.txt"
    numbers = read_numbers_from_file(file_name)

    if numbers:
        total, average = calculate_sum_and_average(numbers)
        print(f"Numbers: {numbers}")
        print(f"Sum: {total}")
        print(f"Average: {average:.2f}")
    else:
        print("No valid numbers to process.")
