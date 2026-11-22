# Print my header information
print("\n")
print("\"1 December 1918\" University of Alba Iulia")
print("Computer Science Department")
print("Course: Fundamental Algorithms")
print("Lab 6: Question 1 - Implementation of Insertion Sort Algorithm Reading input from a file")
print("By: Osatohanmwen Davidson Ikponmwenosa")
print("\n")


# ---------------------------------------------------------
# Implement 2 sorting algorithms of your choice (for example, Insertion Sort, Merge Sort, 
# Do not use sorted() or list.sort() to perform the sorting. 
# • Sort the numbers in ascending order. At each run, the program must execute only the 
# algorithm specified in the file. 
# • Read exactly two lines from date.txt: line 1 contains the integers separated by spaces, and 
# line 2 contains the name of the selected algorithm (for example, Insertion, Merge, or 
# Quick). Do not read the number of elements separately. 
# • Check that the file exists, that the numbers are valid, and that the specified algorithm is 
# oneof those implemented. Display a clear message for invalid input. 
# • Write the result of the selected algorithm to the same file, below the two input lines, 
# labeling it with the algorithm's name. Preserve the original input data.
# ---------------------------------------------------------


import numpy as np
import os


# function to read numbers and algorithm name from the file
def read_numbers_from_file(filename):

    if not os.path.exists(filename):

        print(f"Error: The file '{filename}' could not be found.")

        return None, None
    
    with open(filename, "r") as file:

        lines = file.readlines()

    if len(lines) < 2:

        print("Error: The file is incomplete. It must contain at least two lines.")

        return None, None
        
    return lines[0].strip(), lines[1].strip()


# function to validate the numbers and algorithm name
def validate_and_parse(numbers_line, algorithm_name):

    parts = numbers_line.split()
    
    if not parts:

        print("Error: Line 1 cannot be empty.")

        return None, None

    # checking if all parts are valid integers
    for x in parts:
        if not x.lstrip('-').isdigit():
            print(f"Error: '{x}' is not a valid integer.")
            return None, None

    # converting the valid parts to a NumPy array of integers
    numbers = np.array([int(x) for x in parts])

    # checking if the algorithm name is supported
    supported_algorithms = ["Insertion", "Merge"]
    if algorithm_name not in supported_algorithms:
        print(f"Error: '{algorithm_name}' is not supported. Choose from: {supported_algorithms}")
        return None, None

    return numbers, algorithm_name




def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        position = numbers[i]
        j = i - 1
        while j >= 0 and position < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = position
    return numbers



# function to write the sorted numbers and algorithm name to the file
def write_sorted_numbers_to_file(filename, sorted_numbers, algorithm_name):
    with open(filename, "a") as file:
        file.write(f"\nSorted numbers using {algorithm_name} Sort:\n")
        file.write(" ".join(map(str, sorted_numbers)) + "\n")   


# mail function 
def main():
    filename = input("Enter the filename (e.g., date.txt): ").strip()
    
    # read numbers and algorithm name from the file
    line1, line2 = read_numbers_from_file(filename)
    if line1 is None or line2 is None:
        return

    # validating the numbers and algorithm name
    numbers, algorithm_name = validate_and_parse(line1, line2)
    if numbers is None or algorithm_name is None:
        return

    print(f"Selected Algorithm: {algorithm_name}")
    print("Original numbers:", numbers)

    # calling the sorting algorithm based on the specified algorithm name
    sorted_numbers = insertion_sort(numbers)
    print("Sorted numbers:", sorted_numbers)

    # adding the sorted numbers and algorithm name to the file
    write_sorted_numbers_to_file(filename, sorted_numbers, algorithm_name)
    print(f"Results successfully appended to {filename}.")


if __name__ == "__main__":
    main()

